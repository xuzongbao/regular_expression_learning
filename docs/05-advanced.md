# 进阶索引与引擎差异

上一章：[什么时候不该用正则](04-caveats.md) · [目录](../README.md) · 下一章：[.NET 附录](99-appendix-dotnet.md)

本章目录：

- [进阶索引](#进阶索引)
- [附录 B 引擎差异速查](#附录-b-引擎差异速查)

---

## 进阶索引

主路径用不到时，不必先记熟。需要再查手册。下列按 PCRE 默认理解；.NET 专有已标出。

| 模式 | 含义 | 引擎 |
| --- | --- | --- |
| `\t` `\n` `\r` `\f` `\v` | Tab / 换行 / 回车 / 换页 / 垂直 Tab | 通用(PCRE) |
| `\a` | BEL（响铃） | 通用(PCRE) |
| `\e` | Escape | 通用(PCRE)；JS 字符串里含义不同 |
| `\b` | 在字符类 **外面**是单词边界；写在 `[]` **里面**是退格 | 通用(PCRE) |
| `\xnn` | 十六进制字节 | 通用(PCRE) |
| `\unnnn` | Unicode 码位（四位十六进制） | **.NET / JS**；PCRE 更常用 `\x{…}` |
| `\cN` | 控制字符，如 `\cC` 表示 Ctrl+C | 通用(PCRE) |
| `\A` | 整串开头，不受 `m` 影响 | 通用(PCRE)；JS 无 `\A` |
| `\Z` | 整串结尾或最后那个换行前 | 通用(PCRE) |
| `\z` | 真正的整串结尾 | 通用(PCRE) |
| `\G` | 上一次匹配结束的位置 | PCRE / .NET / Java；JS 无 |
| `\p{L}` `\p{N}` `\p{Han}` | Unicode 属性 | PCRE 开 Unicode 后常用。`.NET` 示例里的 `\p{IsGreek}` 是 **.NET 命名**；PCRE 写 `\p{Greek}` |
| `(?>exp)` | 原子组：这一段匹配后不回溯 | PCRE / .NET / Java；JS 无此语法。教学见 [什么时候不该用正则](04-caveats.md#什么时候不该用正则) |
| `(?imnsx:exp)` / `(?imnsx)` | 局部或之后改变修饰符 | 通用(PCRE)，字母集合因引擎略有出入 |
| `(?(cond)yes\|no)` | 条件：成立走 `yes`，否则 `no` | PCRE / .NET；`cond` 可以是组号、组名或断言 |
| `(?(name)yes)` | 同上，失败分支为空 | 通用(PCRE) 条件语法；**拿它当「堆栈空了没」检查是 .NET 平衡组用法** |
| `(?R)` / `(?1)` | 递归整式或某个捕获组 | **PCRE** 嵌套括号常用这个，而不是平衡组 |
| `(?<x>-<y>exp)` | 平衡组 | `（.NET 专有 / 非 PCRE 默认）` 见 [附录 A](99-appendix-dotnet.md) |

---

## 附录 B 引擎差异速查

| 话题 | PCRE / PCRE2（本文默认） | 其他 |
| --- | --- | --- |
| `\w` `\b` | 默认 ASCII | .NET、Python 3 更偏 Unicode；JS 默认 ASCII |
| 汉字 | 不要默认 `\w` 能匹配汉字 | .NET 常常可以 |
| 命名组 | `(?<n>…)` / `(?'n'…)`，`\k<n>` | Python：`(?P<n>…)` / `(?P=n)` |
| 后行断言 | PCRE2 允许变长 | Python `re` 多要求定长；旧 JS 没有 |
| 嵌套配对 | 递归 `(?R)` | .NET：平衡组 |
| 试模式 | regex101 选 PCRE2；修饰符见 [标志与选项对照表](02-groups-and-lookaround.md#标志与选项对照表) | 最终仍要以你代码里的引擎为准 |

---

上一章：[什么时候不该用正则](04-caveats.md) · [目录](../README.md) · 下一章：[.NET 附录](99-appendix-dotnet.md)
