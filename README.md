# regular_expression_learning
正则表达式学习笔记

# 元字符

- ## 常用元字符
	- <font color=red size=4>.</font>  : 匹配除换行符以外的任意字符
	- <font color=red size=4>\w</font> : 匹配字母或数字或下划线或汉字
	- <font color=red size=4>\s</font> : 匹配任意的空白符
	- <font color=red size=4>\d</font> : 匹配数字
	- <font color=red size=4>\b</font> : 匹配单词的开始或结束
	- <font color=red size=4>^</font>  : 匹配字符串的开始
	- <font color=red size=4>$</font>  : 匹配字符串的结束
	
- ## 常用元字符例子
	- <font color=red size=4>\ba\w*\b</font></red> : 匹配以字母a开头的单词——先是某个单词开始处（\b），然后是字母a，然后是任意数量的字母或数字（\w*），最后是单词结束处（\b）。
	- <font color=red size=4>\d+</font></red> : 匹配1个或更多连续的数字，这里的+是和*类似的元字符，不同的是*匹配重复任意次（可能是0）而+则匹配重复1次或更多次。
	- <font color=red size=4>\b\w{6}\b</font> : 匹配刚好6个字符的单词。
	- <font color=red size=4>^\d{5,12}$</font> :匹配5位到12位数字

# 字符转义

- ## 字符转义

	- <font color=red size=4>\</font> : 字符转义
	 
- ## 字符转义例子
	- <font color=red size=4>\ . </font>  :匹配" . "。 
	- <font color=red size=4>\ * </font>  :匹配" * "。 
	- <font color=red size=4>\ \ </font>  :匹配" \ "。 
	
# 重复

- ## 常用重复限定符

	- <font color=red size=4> * </font> : 重复零次或更多次
	- <font color=red size=4> + </font> : 重复一次或更多次
	- <font color=red size=4> ? </font> : 重复零次或一次
	- <font color=red size=4> {n} </font> : 重复n次
	- <font color=red size=4> {n,} </font> : 重复n次或更多次
	- <font color=red size=4> {n,m} </font> : 重复n到m次
	 
- ## 常用重复限定符例子
	- <font color=red size=4> Windows\d+ </font>  : 匹配Windows后面跟1个或更多数字。 
	- <font color=red size=4> ^\w+ </font>  : 匹配一行的第一个单词（或整个字符串的第一个单词，具体匹配哪个意思得看选项设置）。 

# 字符类
	 
- ## 常用字符类例子
	- <font color=red size=4> [aeiou] </font>  : 匹配任何一个英文元音字母。 
	- <font color=red size=4> [.?!] </font> : 匹配标点符号（。或？或！）。
	- <font color=red size=4> [0-9] </font>  : 和<font color=red size=4> \d </font>同一个意思。
	- <font color=red size=4> [a-z0-9A-Z] </font> : 同 <font color=red size=4> \w </font>。
	- <font color=red size=4> \ (?0\d{2}[) -]?\d{8} </font> : 匹配几种格式的电话号码

# 分枝条件 <font size=4>（正则表达式里的分支条件指的是有几种规则，如果满足其中任意一种规则都应该当成匹配，具体方法是用 | 把不同的规则分隔开。）</font>

- ## 常用分枝条件例子
	- <font color=red size=4> 0\d{2}-\d{8} | 0\d{3}-\d{7} </font>  : 匹配两种以连字号分割的电话号码：一种是三位区号，8位本地号（如010-12345678），一种是4位区号，7位本地号（0376-1234567）。 
	- <font color=red size=4> \(?0\d{2})?[- ]?\d{8} | 0\d{2}[- ]?\d{8} </font>  : 匹配3位区号的电话号码，其中区号可以用小括号括起来，也可以不用，区号与本地号间可以用连字号或空格间隔，也可以没有间隔。
	- <font color=red size=4> \d{5}-\d{4} | \d{5} </font> : 匹配美国的邮政编码。美国邮编的规则是5位数字，或者用连字号间隔的9位数字。这里需要注意的是：<font color=blue>使用分枝条件时，要注意各个条件的顺序。</font>如果改成<font color=red size=4> \d{5} | \d{5}-\d{4}  </font>的话，那么就只会匹配5位数的邮编（以及9位邮编的前5位）。原因是匹配分枝条件时，将会从左到右地测试每个条件，如果满足了某个分枝的话，就不会去再管其他的条件了。

# 分组

- ## 常用分组例子
	- <font color=red size=4> (\d{1,3\ .}{3}\d{1.3}) </font>  : 匹配一个简单的IP地址匹配表达式。<font color=blue>\d{1,3}</font>匹配1到3位的数字，<font color=blue>(\d{1,3}\ .)</font>{3}匹配三位数加上一个英文句号（这个整体也就是这个分组的）重复次数，最后再加上一个一到三位的数字<font color=blue>(\d{1,3})</font> 。但是这个表达式也讲匹配256.300.888.999这种不可能存在的IP地址。
	- <font color=red size=4> ((2[0-4]\d|25[0-5]|[01]?\d\d?)\ .){3}(2[0-4]\d|25[0-5]|[01]?\d\d?) </font> : 这个才是正确的匹配IP地址的正则表达式。

# 反义

- ## 常用反义代码

	- <font color=red size=4> \W </font> : 匹配任意不是字母，数字，下划线，汉字的字符
	- <font color=red size=4> \S </font> : 匹配任意不是空白的字符
	- <font color=red size=4> \D </font> : 匹配任意非数字的字符
	- <font color=red size=4> \B </font> : 匹配不是单词开头或结束的位置
	- <font color=red size=4> [^x] </font> : 匹配除了x以外的任意字符
	- <font color=red size=4> [^aeiou] </font> : 匹配除了aeiou这几个字母以外的任意字符
	 
- ## 常用反义代码例子
	- <font color=red size=4> \S+ </font>  : 匹配不包括空白符的字符串。 
	- <font color=red size=4> <a[^>]+> </font>  : 匹配用尖括号括起来的以a开头的字符串。 

# 反向引用

- ## 常用分组语法

	- 捕获
		- <font color=red size=4> (exp) </font> : 匹配exp，并捕获文本到自动命名的组里
		- <font color=red size=4> (?(name)exp) </font> : 匹配exp，并捕获文本到名称为name的组里，也可以写成(?'name'exp)
		- <font color=red size=4> (?:exp) </font> : 匹配exp，不捕获匹配的文本，也不给此分组分配组号
	- 零宽断言
		- <font color=red size=4> (?=exp) </font> : 匹配exp前面的位置
		- <font color=red size=4> (?<=exp) </font> : 匹配exp后面的位置
		- <font color=red size=4> (?!exp) </font> : 匹配后面跟的不是exp的位置
		- <font color=red size=4> (?<!exp) </font> : 匹配前面不是exp的位置
	- 注释
		- <font color=red size=4> (?#comment) </font> : 这种类型的分组不对正则表达式的处理产生影响，用于提供注释让人阅读

- ## 常用反义代码例子
	- <font color=red size=4> \b(\w+)\b\s+\1\b </font>  : 匹配重复的单词，像go go或者kitty kitty等。这个表达式首先是一个单词，也就是单词开始处和结束处之间的多于一个的字母或者数字(\b(\w+)\b)，这个单词会被捕获到编号为1的分组中，然后是1个或几个空白符(\s+)，最后是分组1中捕获的内容(也就是前面匹配的八个单词)(\1)。
	- <font color=red size=4> \b(?<Word>\w+)\b\s+\k<Word>\b </font>  : 同上，只是组名定义为Word了。
	- <font color=red size=4> (?=exp) </font>  : 这个也就零宽度正预测先行断言，它断言自身出现的位置的后面能匹配表达式exp。比如\b\w+(?=ing)\b)，匹配以ing结尾的单词的前面部分（除了ing以外的部分），如查找I'm singing while you are dancing时，它会匹配sing和danc。 
	- <font color=red size=4> (?<=exp) </font>  : 这个也叫零宽度正回顾后发断言，它断言自身出现的位置的前面能匹配表达式exp。比如(?<=\bre)\w+\b，匹配以re开头的单词的后半部分(除了re以外的部分)，例如在查找reading a book时，它匹配ading。
	- <font color=red size=4> ((?<=\d)\d{3})+\b </font>  : 匹配一串很长的数字中从右到左每三个数字加一个逗号的位置。
	- <font color=red size=4> (?<=\s)\d+(?=\s) </font>  : 匹配以空白符间隔的数字(不包括这些空白符)。
	- <font color=red size=4> \b\w*q[^u]\w*\b </font>  : 匹配包含后面不是字母u的字母q的单词。但是如果多做测试(或者你思维足够敏锐，直接就观察出来了)，你会发现，如果q出现在单词的结尾的话，像Iraq,Benq，这个表达式就会出错。这是因为[^u]总要匹配一个字符，所以如果q是单词的最后一个字符的话，后面的[^u]将会匹配q后面的单词分隔符(可能是空格，或者是句号或其它的什么)，后面的\w*\b将会匹配下一个单词，于是\b\w*q[^u]\w*\b就能匹配整个Iraq fighting。负向零宽断言能解决这样的问题，因为它只匹配一个位置，并不消费任何字符。现在，我们可以这样来解决这个问题：\b\w*q(?!u)\w*\b。
	- <font color=red size=4> (?!exp) </font>  : 零宽度负预测先行断言，断言此位置的后面不能匹配表达式exp。例如:\d{3}(?!\d)匹配三位数字，而且这三位数字的后面不能是数字；\b((?!abc)\w)+\b匹配不包含连续字符abc的单词。
	- 同理，我们可以用(?<!exp),零宽度负回顾后发断言来断言此位置的前面不能匹配表达式exp：(?<![a-z])\d{7}匹配前面不是小写字母的七位数字。
	- <font color=red size=4> (?<=(\w+)>).*(?=<\/\1) </font>  : 匹配不包含属性的简单HTML标签内的内容。<font color=blue>(?<=(\w+)>)</font>指定了这样的前缀：被尖括号括起来的单词（比如可能是<b>），然后是.*（任意的字符串），最后是一个后缀(?=<\/\1)。注意后缀里的\/，它用到了前面提过的字符转义；\1则是一个反向引用，引用的正是捕获的第一组，前面的(\w+)匹配的内容，这样如果前缀实际上是<b>的话，后缀就是<b>了。整个表达式匹配的是<b>和<b>之间的内容（再次提醒，不包括前缀和后缀本身）。
	- 注释
		- <font color=red size=3> (?<=    # 断言要匹配的文本的前缀 </font>
		- <font color=red size=3> <(\w+)> # 查找尖括号括起来的字母或数字(即HTML/XML标签) </font>
		- <font color=red size=3> )       # 前缀结束 </font>
		- <font color=red size=3> .*      # 匹配任意文本 </font>
		- <font color=red size=3> (?=     # 断言要匹配的文本的后缀 </font>
		- <font color=red size=3> <\/\1>  # 查找尖括号括起来的内容：前面是一个"/"，后面是先前捕获的标签 </font>
		<font color=red size=3> )       # 后缀结束 </font>

- # 贪婪与懒惰

	- 懒惰限定符 
		- <font color=red size=4> *? </font> : 重复任意次，但尽可能少重复
		- <font color=red size=4> +? </font> : 重复1次或者更多次，但尽可能少重复
		- <font color=red size=4> ?? </font> : 重复0次或1次，但尽可能少重复
		- <font color=red size=4> {n,m}? </font> : 重复n到m次，但尽可能少重复
		- <font color=red size=4> {n,}? </font> : 重复n次以上，但尽可能少重复

	- 贪婪与懒惰例子

		- 当正则表达式中包含能够接收重复的限定符时，通常的行为是（在使整个表达式能得到匹配的前提下）**__匹配尽可能多__**的字符。以这个表达式为例：a.*b，它将会匹配最长的以a开始，以b结束的字符串。如果用它来搜索aabab的话，它会整个字符串aabab。这被称为贪婪匹配。
		- 有时，我们需要懒惰匹配，也就是匹配尽可能少的字符。前面给出的限定符都可以被转化成懒惰匹配模式，只要在它后面加上一个问号?。这样<font color=red> .*? </font>就意味着匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复。
		- <font color=red size=4> a.*?b </font> : 匹配最短的，以a开始，以b结束的字符串。如果它应用于aabab的话，它会匹配aab（第一到三个字符）和ab（第四到第五个字符）。

- # 处理选项

	- 常用的处理选项

		- <font color=red size=4> IgnoreCase(忽略大小写) </font> : 匹配时不区分大小写。
		- <font color=red size=4> Multiline(多行模式) </font> : 更改^和$的含义，使它们分别在任意一行的行首和行尾匹配，而不仅仅在整个字符串的开头和结尾匹配。(在此模式下,$的精确含意是:匹配\n之前的位置以及字符串结束前的位置.)
		- <font color=red size=4> Singleline(单行模式) </font> : 更改.的含义，使它与每一个字符匹配（包括换行符\n）。
		- <font color=red size=4> IgnorePatternWhitespace(忽略空白) </font> : 忽略表达式中的非转义空白并启用由#标记的注释。
		- <font color=red size=4> ExplicitCapture(显式捕获) </font> : 仅捕获已被显式命名的组。

- # 平衡组/递归匹配

	- 有时我们需要匹配像( 100 * ( 50 + 15 ) )这样的可嵌套的层次性结构，这时简单地使用\(.+\)则只会匹配到最左边的左括号和最右边的右括号之间的内容(这里我们讨论的是贪婪模式，懒惰模式也有下面的问题)。假如原来的字符串里的左括号和右括号出现的次数不相等，比如( 5 / ( 3 + 2 ) ) )，那我们的匹配结果里两者的个数也不会相等。有没有办法在这样的字符串里匹配到最长的，配对的括号之间的内容呢？
	- 为了避免(和\(把你的大脑彻底搞糊涂，我们还是用尖括号代替圆括号吧。现在我们的问题变成了如何把xx <aa <bbb> <bbb> aa> yy这样的字符串里，最长的配对的尖括号内的内容捕获出来？
	- 这里需要用到以下的语法构造：
		- <font color=red size=4 > (?'group') </font> : 把捕获的内容命名为group,并压入堆栈(Stack)
		- <font color=red size=4 > (?'-group') </font> : 从堆栈上弹出最后压入堆栈的名为group的捕获内容，如果堆栈本来为空，则本分组的匹配失败
		- <font color=red size=4 > (?(group)yes|no) </font> : 如果堆栈上存在以名为group的捕获内容的话，继续匹配yes部分的表达式，否则继续匹配no部分
		- <font color=red size=4> (?!) </font> : 零宽负向先行断言，由于没有后缀表达式，试图匹配总是失败

- # 尚未详细讨论的语法

	- <font color=red size=4> \a </font> : 报警字符(打印它的效果是电脑嘀一声)。
	- <font color=red size=4> \b </font> : 通常是单词分界位置，但如果在字符类里使用代表退格。
	- <font color=red size=4> \t </font> : 制表符，Tab。
	- <font color=red size=4> \r </font> : 回车。
	- <font color=red size=4> \v </font> : 竖向制表符。
	- <font color=red size=4> \f </font> : 换页符。
	- <font color=red size=4> \n </font> : 换行符。
	- <font color=red size=4> \e </font> : Escape。
	- <font color=red size=4> \0nn </font> : ASCII代码中八进制代码为nn的字符。
	- <font color=red size=4> \xnn </font> : ASCII代码中十六进制代码为nn的字符。
	- <font color=red size=4> \unnnn </font> : Unicode代码中十六进制代码为nnnn的字符。
	- <font color=red size=4> \cN </font> : ASCII控制字符。比如\cC代表Ctrl+C。
	- <font color=red size=4> \A </font> : 字符串开头(类似^，但不受处理多行选项的影响)。
	- <font color=red size=4> \Z </font> : 字符串结尾或行尾(不受处理多行选项的影响)。
	- <font color=red size=4> \z </font> : 字符串结尾(类似$，但不受处理多行选项的影响)。
	- <font color=red size=4> \G </font> : 当前搜索的开头。
	- <font color=red size=4> \p{name} </font> : Unicode中命名为name的字符类，例如\p{IsGreek}。
	- <font color=red size=4> (?>exp) </font> : 贪婪子表达式。
	- <font color=red size=4> (?<x>-<y>exp) </font> : 平衡组。
	- <font color=red size=4> (?im-nsx:exp </font> : 在子表达式exp中改变处理选项。
	- <font color=red size=4> (?im-nsx) </font> : 为表达式后面的部分改变处理选项。
	- <font color=red size=4> (?(exp)yes|no) </font> : 把exp当作零宽正向先行断言，如果在这个位置能匹配，使用yes作为此组的表达式；否则使用no。
	- <font color=red size=4> (?(exp)yes) </font> : 同上，只是使用空表达式作为no。
	- <font color=red size=4> (?(name)yes|no) </font> : 如果命名为name的组捕获到了内容，使用yes作为表达式；否则使用no。
	- <font color=red size=4> (?(name)yes) </font> : 同上，只是使用空表达式作为no。



