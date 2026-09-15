# 可验证的正则速查 / 学习笔记

Verifiable regex cheat sheet and study notes (Chinese). Not a full textbook.

这份仓库是**可验证的正则速查和学习笔记**，用来对照语法、改错例子、在 [regex101](https://regex101.com/) 上亲手试。它**不是**一本完整教材，也**不是**要和长篇入门文章抢定位。

章节骨架高度接近经典中文教程《正则表达式30分钟入门教程》。本仓库做的是：**整理、勘误、补上能对上号的匹配/不匹配例子**。完整叙述请读原文（见 [参考与致谢](#参考与致谢)）。本仓库以 **MIT** 协议开源，见 [许可证](#许可证) 与根目录 [`LICENSE`](LICENSE)。

教学正文在 [`docs/`](docs/)；本页只做导航：定位、默认引擎、目录、怎么跑校验。

---

## 这份笔记是什么

| 是 | 不是 |
| --- | --- |
| 速查 + 学习笔记 | 30 分钟读完的完整教材 |
| 可验证的例子（先写测试字符串，再写模式） | 只靠记忆背语法 |
| 在经典大纲上的勘误与补例 | 宣称独自发明了这一套章节 |
| 默认讲 **通用语法 / PCRE 风格** | 默认讲 .NET，或保证 JS / Python / Java 行为完全一样 |

适合：已经知道「正则能用来找文本规则」，想把语法对上可运行的例子，也想知道什么时候不该硬上正则。不适合第一次听说正则——请先看鹿鸣（deerchao）的原文。

展开（含阅读约定和开场例子）：[入门：定位、引擎、验证](docs/00-getting-started.md)。

---

## 默认引擎

**默认按通用语法 / PCRE 风格讲解。** 在 [regex101](https://regex101.com/) 验证时，左栏 Flavor 请选 **PCRE** 或 **PCRE2**。

同一串模式在 JS / Python `re` / Java / .NET 里可能不同（`\w` 宽窄、后行是否定长、命名组写法）。文中凡是 **.NET 才能用、PCRE 默认没有** 的特性，标成 `（.NET 专有 / 非 PCRE 默认）`。平衡组等较重的 .NET 内容在 [附录 A](docs/99-appendix-dotnet.md)；对照表见 [附录 B](docs/05-advanced.md#附录-b-引擎差异速查)。

未特别说明时：区分大小写、`.` 不匹配换行、`\w` 按 PCRE 默认是 `[A-Za-z0-9_]`（**不含汉字**）。

---

## 文档目录

前几章把语法对上例子；实战模式动手；然后是刹车——学完「能写」之后，再记住「不该写」。改正文里的 ✓ / ✗ 时，请同步 [`examples.yml`](examples.yml) 并看 [如何运行校验](#如何运行校验)。

| 文件 | 内容 |
| --- | --- |
| [docs/00-getting-started.md](docs/00-getting-started.md) | 定位、引擎、regex101 怎么对拍、阅读约定、[从例子开始](docs/00-getting-started.md#从例子开始)、[本文修正过什么](docs/00-getting-started.md#本文修正过什么) |
| [docs/01-basics.md](docs/01-basics.md) | [元字符](docs/01-basics.md#元字符)、[字符转义](docs/01-basics.md#字符转义)、[重复（量词）](docs/01-basics.md#重复量词)、[字符类](docs/01-basics.md#字符类)、[分枝条件](docs/01-basics.md#分枝条件) |
| [docs/02-groups-and-lookaround.md](docs/02-groups-and-lookaround.md) | [分组](docs/02-groups-and-lookaround.md#分组)、[反义](docs/02-groups-and-lookaround.md#反义)、[反向引用](docs/02-groups-and-lookaround.md#反向引用)、[环视](docs/02-groups-and-lookaround.md#环视零宽断言)、[贪婪与懒惰](docs/02-groups-and-lookaround.md#贪婪与懒惰)、[注释](docs/02-groups-and-lookaround.md#注释)、[标志与选项对照表](docs/02-groups-and-lookaround.md#标志与选项对照表) |
| [docs/03-cookbook.md](docs/03-cookbook.md) | [常用实战模式](docs/03-cookbook.md#常用实战模式)（邮箱 / 手机号 / 日期 / URL 味道 / 整数小数） |
| [docs/04-caveats.md](docs/04-caveats.md) | [什么时候不该用正则](docs/04-caveats.md#什么时候不该用正则)（含 ReDoS 说明） |
| [docs/05-advanced.md](docs/05-advanced.md) | [进阶索引](docs/05-advanced.md#进阶索引)、[附录 B 引擎差异速查](docs/05-advanced.md#附录-b-引擎差异速查) |
| [docs/99-appendix-dotnet.md](docs/99-appendix-dotnet.md) | [附录 A NET 专有平衡组与递归匹配](docs/99-appendix-dotnet.md#附录-a-net-专有平衡组与递归匹配) |

---

## 怎么验证

1. 打开 [https://regex101.com/](https://regex101.com/)
2. Flavor 选 **PCRE2**
3. **先在 TEST STRING 里写要匹配的文本**，再写 Regular Expression
4. 对照 `docs/` 里的 ✓ 匹配 / ✗ 不匹配；若结果对不上，先看「引擎」一行，再看是否勾了 `i` / `m` / `s` / `u` 等修饰符（对照见 [标志与选项对照表](docs/02-groups-and-lookaround.md#标志与选项对照表)）

不要只看模式「长得对」。正则难的是边界：多一个空格、少一个转义、引擎不同，结果都会变。更完整的步骤见 [怎么验证](docs/00-getting-started.md#怎么验证)。

---

## 如何运行校验

`docs/` 里的 ✓ / ✗ 抽了一份到 [`examples.yml`](examples.yml)，用脚本自动跑，避免笔记和真实引擎各说各话。

**CI 用的引擎接近 PCRE2，但不是 regex101 的完整复刻。** GitHub Actions（`ubuntu-latest`）跑的是 **Python 3 + [`pcre2`](https://pypi.org/project/pcre2/) 包**（捆绑 libpcre2，比标准库 `re`、也比 PyPI 上的 `regex` 库更接近本文默认引擎），并默认加上 `ASCII`，让 `\w` / `\d` / `\b` 接近文中说的 PCRE 默认（**不含汉字**）。这和 JavaScript `RegExp`、Python `re`、以及 regex101 上每一个勾选项都可能有边角差别。递归 `(?R)`、.NET 平衡组不会放进这份会执行的清单。

本地（仓库根目录）：

```bash
python3 -m pip install -r requirements-ci.txt
python3 scripts/check_examples.py
```

失败时脚本会打印是哪一条 `id`、哪一个测试字符串不符合。往 `examples.yml` 增补用例后，请在本地跑通再推送；推到 `master` 的 push / pull request 也会跑 [`.github/workflows/ci.yml`](.github/workflows/ci.yml)。

灾难性回溯那种教学模式（如 `^(a+)+$`）只写在清单里作文档，标了 `skip: true`，**不会**在 CI 里当计时炸弹执行。变长且含捕获的后行（正文里的 `(?<=<(\w+)>).*?(?=</\1>)`）同样跳过：CI 用的 PCRE2 绑定会拒绝无限长后行；请用旁边那条不依赖后行的 `<(\w+)>(.*?)</\1>` 来对拍，或到 regex101 选 PCRE2 手试。

---

## 参考与致谢

本章节顺序与大量讲解，来自鹿鸣（deerchao）的经典教程：

**[正则表达式30分钟入门教程](https://deerchao.cn/tutorials/regex/regex.htm)**  
（亦广泛转载于 [runoob 镜像](https://www.runoob.com/regexp/regexp-tutorial.html) 等站点）

原文作者在文中说明：教程介绍的是 **.NET** 下的正则行为。本笔记**不宣称独自撰写了这一大纲**，而是把它当作公共教学骨架，改成 PCRE 默认、修好损坏的例子，并补上可核对的匹配样本。若你需要完整行文、边注和更新记录，请阅读原文；本文不能代替它。

---

## 许可证

本仓库以 [MIT License](LICENSE) 发布。你可以自由使用、复制、修改和分发这些笔记，只需保留版权声明和许可文本。完整条款见根目录 [`LICENSE`](LICENSE)。

Copyright (c) 2016-2026 xuzongbao
