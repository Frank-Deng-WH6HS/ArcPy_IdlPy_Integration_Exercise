Markdown语法示例: 字体和段落\
Samples of Markdown Syntax: Font and Paragraphs

***

# 标题样式 / Style of Headings

# 第1级标题(脚本行以单个"\#"号打头, 后接一个半角空格)
# Level-1 Heading(Script Line begins with a single slot char. , followed by a whitespace char. )

## 第2级标题(脚本行以2个"\#"号打头, 后接一个半角空格)
## Level-2 Heading(Script Line begins with 2 slot char. , followed by a whitespace char. )

### 第n级标题(脚本行以n个"\#"号打头, 后接一个半角空格, 最多支持6级标题)
### Level-n Heading(Script Line begins with n slot char. , up to 6, followed by a whitespace char. )

***

# 正文样式 / Style of Body Text

## 正文中特殊字符的转义 / Escaping of Special Characters in Body Text
Markdown脚本行以连续7个以上的"\#"打头, 会被解析为正文. \
A script line beginning with 7 or more continuous \#'s will be interpreted as body text. 

正文行首不建议设置其他符号. 如无法避免, 需在符号前使用"\\"(反斜杠)进行转义. \
Placing other symbols at the beginning of body text is not recommended. Use backslash to escape these symbols if inevitable. \
例如以下文本会被解释为正文, 而非标题: \
\# 这是正文, 不是任何级别的标题. \
1\. 这也是正文, 前面的那些字符不是编号. \
\* 这也是正文, 前面的那些字符不是项目符号. 

## 段落分隔符与(渲染)行分隔符 / Paragraph and (Rendered) Line Separators
同一Markdown文件的不同标题, 以及标题与正文, 分属不同的段落. \
Different headings, or headings and body texts, are considered as different paragraphs. 

Markdown脚本文件中, 空行(行内没有任何字符)的功能相当于段落分隔符(即"硬回车"), 段落分隔符前后的文本分属于两个段落. \
A blank script line (a script line without any character) in Markdown files acts as paragraph separator (i.e. "Hard return"), separating texts before and after it into different paragraphs. 

当反斜杠位于脚本行的尾部时, 其功能相当于行分隔符(即"软回车"), 行分隔符前后的文本位于同一段落内. \
Backslash acts as (rendered) line separator (i.e. "Soft return") when placed at the end of one line, 
while texts before and after it are in the same paragraph. 

行分隔符不适用于各级标题. \
Line separators are not valid in headings of any levels. 

后续语法示例中涉及到的编号, 项目符号, 检查单, 以及各类高级文本块, 其样式的应用, 均**以段落为单位**. \
The appliance of styles of numbering, bullets, checklists, and advanced text blocks, acts **by paragraph**. 

***

# 字体, 编号, 项目符号和检查单 / Font, Numbering, Bullets, and Checklists

## 字体样式 / Font Styles
在正文内插入*斜体*, **粗体**, ***斜体兼粗体***的文本, 需分别将文本首尾使用1, 2, 3个星号括注. \
To insert text with *Italic*, **Bold**, ***Bold and Italic*** style, wrap text with 1, 2, or 3 asterisk(s) respectively. 

在正文内用删除线贯穿~~一段连续的文本~~, 需将文本首尾使用2个"波浪号"括注. \
To strike through ~~a piece of continuous text~~, wrap text with 2 tildes. 

## 编号及其分级 / Numering w/o Multiple Levels
1. 如需在段落中设置编号, 该段落需要以"连续的阿拉伯数字"打头, 后接一个半角句点和一个半角空格. \
    To assign numbering for a paragraph, compose this paragraph beginning with "continuous numerals" followed by a period and a whitespace. 
    
    1. 如果需要设置多级编号, 需使用4的整数倍数目的空格缩进. \
        To assign numbering with multiple levels, indent this line with 4 whitespaces. 
        
        1. 不建议使用"制表符"缩进. \
            Indentition with tabs is not recommended. 
            
        1. 建议在编辑器中配置相关选项, 将制表符自动转化为适当数目的空格. \
            It is recommended to configure certain options in editors to convert tabs into several whitespaces. 
            
    1. 多级编号不能使用类似于论文中"1.2. xxx"的形式, 因为无法被主流的Markdown渲染器正确处理. \
        While numbering with multiple levels, thesis-style formatting ("1.2. xxx") is not allowed, since this format can not be correctly interpreted by mainstream Markdown renderer. 

## 项目符号及其分级 / Bullet w/o Multiple Levels
* 如需在段落中设置"子弹形"的项目符号, 该段落需要以单个"星号, 加号, 或者减号(三者之一)"打头, 后接一个半角空格. \
    To assign bullet for a paragraph, compose this paragraph beginning with a single "asterisk, plus sign, or minus sign" followed by a whitespace. 
    
    * 如果需要设置多级编号, 需使用4的整数倍数目的空格缩进. \
        To assign bullet with multiple levels, indent this line with 4 whitespaces. 

***

# 特殊文本块 / Special Text Blocks

## 代码块 / Code Blocks
### 内嵌代码块
在正文之内嵌入代码, 需要将代码文本首尾使用"抑音符"(又称"反引号")括注. \
To embed codes into body text, use grave accent to wrap the code. \
例如: 在IDL中, `Print, "Hello, world. "`将向控制台另起一行顶格输出"Hello, world. ", 之后光标移至输出行的下一行. 

### 独立代码块
插入独立的代码块(单行或者连续多行), 需要在代码块的首行前和末行后, 分别另起一行, 行内包含三个"抑音符". \
To insert standlone code blocks (single line or continuous multiple lines), insert standlone line consisting with three grave accents before and after the entire code block. \
为使渲染器对代码块进行语法着色(如果可行), 位于代码块前的抑音符后可指定代码语言. \
To apply syntax coloring (if available), assignment of coding language after the three grave accents above the code blocks is allowed. \
例如: 
```IDL 
Pro sample_code
  Print, "Hello, world. "
End
``` 

## $L^AT_EX$ 公式块 / $L^AT_EX$ Formulae
### 内嵌公式块
在正文之内嵌入LaTeX公式, 需要将公式首尾使用"美元符号"括注. \
To embed LaTeX formulae into body text, use dollar sign to wrap the formula. \
例如: 在匀变速直线运动中, $v^2 - v_0^2 = 2 a x$ 揭示了位移量与初末速度之间的关系. 

### 独立公式块
插入独立的LaTeX公式块(单行或者连续多行), 需要在公式块的首行前和末行后, 分别另起一行, 行内包含两个"美元符号". \
To insert standlone LaTeX formula blocks (single line or continuous multiple lines), insert standlone line consisting with two dollar signs before and after the entire formula block. \
例如: 关于 $x$ 的一元二次方程 $$a x^2 + b x + c = 0 ~ (a \ne 0)$$ 的两个复数根为 $$x_{1, 2} = {{- b \pm \sqrt{b^2 - 4 a c}} \over {2 a}}$$. 

## 引用块 / Referrence Blocks
> 第1级引用(段落以单个">"号打头, 后接一个半角空格). \
    Level-1 Referrence block(Paragraph begins with a single "greater than" sign, followed by a whitespace char. ). 

>> 第2级引用(段落以2个">"号打头, 后接一个半角空格). \
    Level-2 Referrence block(Paragraph begins with 2 "greater than" signs, followed by a whitespace char. ). 

>>> 第n级引用(段落以n个">"号打头, 后接一个半角空格). \
    Level-n Referrence block(Paragraph begins with n "greater than" signs, followed by a whitespace char. ). 

> 当**连续多个脚本行(不包含段落分隔符)**\指定为**相同级别**的引用时, 形成该级别下的引用块. \
> While **Multiple continuous script lines w/o paragraph separator** are assigned as referrences of **same level**, they form sinto a referrence block of current level. 
>> 当**连续多个脚本行(不包含段落分隔符)**\指定为**不同级别**的引用时, 形成嵌套的引用块. 
>> While **Multiple continuous script lines w/o paragraph separator** are assigned as referrences of **different levels**, they form into a referrence block of nested level. 
>
> 从嵌套的引用块中跳出至上一级别时, 需在中间插入与跳出后级别相同的一个脚本行(内容留空). \
To step out to the previous level from nested referrence blocks, insertion of a new script line with the same level (with item remainied empty) is required. 

> Markdown的其他语法, 例如**字体样式**, $L^AT_EX$公式块, `代码块`等, 适用于各级别的引用块内. 
> Other syntaxes of Markdown, such as **font**, $L^AT_EX$ formulae, and `code blocks`, are available in referrence blocks of any level. 
