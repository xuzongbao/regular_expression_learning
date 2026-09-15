#!/usr/bin/env python3
"""校验 examples.yml 是否与 PCRE2 行为一致。

本仓库正文按通用语法 / PCRE 风格讲解。CI 使用 Python 包 pcre2
（捆绑 libpcre2），并默认加上 ASCII，使 \\w / \\d / \\b 接近文中的
PCRE 默认（不含汉字）。这仍不是 regex101 上每一个开关的完整复刻：
变长且含捕获的后行断言、.NET 平衡组、故意的灾难性回溯模式不会执行。

依赖：见仓库根目录 requirements-ci.txt。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Mapping

try:
    import pcre2
    import yaml
except ImportError as exc:  # pragma: no cover - 环境问题在启动时就能发现
    sys.stderr.write(
        "缺少依赖：{}\n请先执行: python3 -m pip install -r requirements-ci.txt\n".format(
            exc
        )
    )
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_EXAMPLES = REPO_ROOT / "examples.yml"

# YAML 1.1 会把未加引号的键 yes/no 读成 true/false。
YES_KEYS = ("yes", True)
NO_KEYS = ("no", False)

FLAG_MAP = {
    "i": pcre2.IGNORECASE,
    "m": pcre2.MULTILINE,
    "s": pcre2.DOTALL,
    "x": pcre2.VERBOSE,
    "a": pcre2.ASCII,
    "u": pcre2.UNICODE,
}

ALLOWED_FLAVORS = {"pcre", "pcre2"}


class CheckError(Exception):
    """单条用例失败（继续跑其余用例，最后汇总退出码）。"""


class SchemaError(Exception):
    """清单格式错误（应立即停）。"""


def _first_present(case: Mapping[str, Any], keys: tuple[Any, ...]) -> Any:
    for key in keys:
        if key in case:
            return case[key]
    return None


def _as_str_list(value: Any, *, field: str, case_id: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise SchemaError(
            "{}: 字段 {} 必须是字符串列表，实际是 {}".format(
                case_id, field, type(value).__name__
            )
        )
    out: list[str] = []
    for i, item in enumerate(value):
        if not isinstance(item, str):
            raise SchemaError(
                "{}: {}[{}] 必须是加引号的字符串，避免 YAML 把数字/yes/no "
                "变成别的类型；实际是 {}: {!r}".format(
                    case_id, field, i, type(item).__name__, item
                )
            )
        out.append(item)
    return out


def _flags_from_str(flags_str: Any, *, case_id: str) -> int:
    """默认 ASCII（PCRE 默认 \\w）。flags 里写 u 则改走 Unicode。"""
    if flags_str is None:
        flags_str = ""
    if not isinstance(flags_str, str):
        raise SchemaError(
            "{}: flags 必须是字符串，例如 i 或 im".format(case_id)
        )
    flags = pcre2.ASCII
    for ch in flags_str:
        if ch == "u":
            flags &= ~pcre2.ASCII
            flags |= pcre2.UNICODE
            continue
        if ch not in FLAG_MAP:
            raise SchemaError("{}: 不认识的 flags 字符 {!r}".format(case_id, ch))
        flags |= FLAG_MAP[ch]
    return flags


def _compile(pattern: str, flags: int, *, case_id: str) -> pcre2.Pattern:
    try:
        return pcre2.compile(pattern, flags)
    except pcre2.PatternError as exc:
        raise CheckError("{}: 模式编译失败: {}".format(case_id, exc)) from exc


def _search(compiled: pcre2.Pattern, text: str) -> Any:
    return compiled.search(text)


def _matched(compiled: pcre2.Pattern, text: str, fullmatch: bool) -> bool:
    if fullmatch:
        return compiled.fullmatch(text) is not None
    return _search(compiled, text) is not None


def _all_matches(compiled: pcre2.Pattern, text: str) -> list[str]:
    return [m.group(0) for m in compiled.finditer(text)]


def check_case(case: Mapping[str, Any], index: int) -> str:
    """成功返回 'pass' 或 'skip'；失败抛 CheckError / SchemaError。"""
    if not isinstance(case, Mapping):
        raise SchemaError("cases[{}] 必须是映射".format(index))

    case_id = case.get("id")
    if not isinstance(case_id, str) or not case_id.strip():
        raise SchemaError("cases[{}] 缺少字符串 id".format(index))

    if case.get("skip"):
        return "skip"

    pattern = case.get("pattern")
    if not isinstance(pattern, str) or pattern == "":
        raise SchemaError("{}: 缺少非空 pattern".format(case_id))

    flavor = case.get("flavor", "pcre")
    if flavor not in ALLOWED_FLAVORS:
        raise SchemaError(
            "{}: flavor={!r} 不是 CI 会执行的 pcre/pcre2；"
            "请改 flavor 或设 skip: true".format(case_id, flavor)
        )

    yes = _as_str_list(_first_present(case, YES_KEYS), field="yes", case_id=case_id)
    no = _as_str_list(_first_present(case, NO_KEYS), field="no", case_id=case_id)
    if "first" in case and not isinstance(case.get("first"), str):
        raise SchemaError("{}: first 必须是字符串".format(case_id))
    if "all" in case and (
        not isinstance(case.get("all"), list)
        or any(not isinstance(x, str) for x in case["all"])
    ):
        raise SchemaError("{}: all 必须是字符串列表".format(case_id))

    if not yes and not no and "first" not in case and "all" not in case:
        raise SchemaError("{}: yes/no/first/all 至少要有一项".format(case_id))

    fullmatch = bool(case.get("fullmatch", False))
    compiled = _compile(
        pattern, _flags_from_str(case.get("flags"), case_id=case_id), case_id=case_id
    )

    for sample in yes:
        if not _matched(compiled, sample, fullmatch):
            kind = "整串匹配" if fullmatch else "查找"
            raise CheckError(
                "{}: 应为匹配（{}）: {!r}".format(case_id, kind, sample)
            )

    for sample in no:
        if _matched(compiled, sample, fullmatch):
            kind = "整串匹配" if fullmatch else "查找"
            raise CheckError(
                "{}: 应为不匹配（{}）: {!r}".format(case_id, kind, sample)
            )

    if "first" in case:
        if not yes:
            raise SchemaError("{}: 写了 first 时 yes 不能为空".format(case_id))
        got = _search(compiled, yes[0])
        if got is None:
            raise CheckError(
                "{}: 无法取第一次匹配，yes[0]={!r} 没有命中".format(
                    case_id, yes[0]
                )
            )
        actual = got.group(0)
        expected = case["first"]
        if actual != expected:
            raise CheckError(
                "{}: 第一次匹配应为 {!r}，实际 {!r}（在 {!r} 上）".format(
                    case_id, expected, actual, yes[0]
                )
            )

    if "all" in case:
        if not yes:
            raise SchemaError("{}: 写了 all 时 yes 不能为空".format(case_id))
        actual_all = _all_matches(compiled, yes[0])
        expected_all = case["all"]
        if actual_all != expected_all:
            raise CheckError(
                "{}: 全部非重叠命中应为 {}，实际 {}（在 {!r} 上）".format(
                    case_id, expected_all, actual_all, yes[0]
                )
            )

    return "pass"


def load_cases(path: Path) -> list[Mapping[str, Any]]:
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise SchemaError("无法读取 {}: {}".format(path, exc)) from exc
    except yaml.YAMLError as exc:
        raise SchemaError("YAML 解析失败: {}".format(exc)) from exc

    if not isinstance(raw, Mapping) or "cases" not in raw:
        raise SchemaError("{} 的顶层必须是含 cases 列表的映射".format(path))
    cases = raw["cases"]
    if not isinstance(cases, list) or not cases:
        raise SchemaError("cases 必须是非空列表")
    return cases


def run(path: Path) -> int:
    print(
        "engine: pcre2 {} (libpcre2 {})  default flags: ASCII".format(
            pcre2.__version__, pcre2.__libpcre2_version__
        )
    )
    print("file: {}".format(path))

    try:
        cases = load_cases(path)
    except SchemaError as exc:
        print("SCHEMA:", exc, file=sys.stderr)
        return 2

    passed = skipped = failed = 0
    seen_ids: set[str] = set()

    for index, case in enumerate(cases):
        try:
            if isinstance(case, Mapping):
                cid = case.get("id")
                if isinstance(cid, str):
                    if cid in seen_ids:
                        raise SchemaError("重复的 id: {}".format(cid))
                    seen_ids.add(cid)
            result = check_case(case, index)
        except SchemaError as exc:
            print("SCHEMA:", exc, file=sys.stderr)
            return 2
        except CheckError as exc:
            print("FAIL:", exc)
            failed += 1
            continue

        case_id = case.get("id", "?")
        if result == "skip":
            skipped += 1
            note = case.get("note") or "skip: true"
            print("SKIP: {}  ({})".format(case_id, note))
        else:
            passed += 1

    print(
        "passed: {}  skipped: {}  failed: {}  total: {}".format(
            passed, skipped, failed, len(cases)
        )
    )
    return 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="用 PCRE2 校验 examples.yml 中的教学用例。"
    )
    parser.add_argument(
        "examples",
        nargs="?",
        default=str(DEFAULT_EXAMPLES),
        help="用例文件（默认：仓库根目录 examples.yml）",
    )
    args = parser.parse_args(argv)
    path = Path(args.examples)
    if not path.is_file():
        print("找不到文件: {}".format(path), file=sys.stderr)
        return 2
    return run(path)


if __name__ == "__main__":
    sys.exit(main())
