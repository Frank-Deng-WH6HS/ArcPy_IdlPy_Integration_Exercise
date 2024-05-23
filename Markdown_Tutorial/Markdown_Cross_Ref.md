Markdown语法示例: 交叉引用\
Samples of Markdown Syntax: Cross-Referencing

***

# 目录 / Table of Contents
在Markdown中建立目录, 需另起一行使用`[TOC]`建立. 此时, 目录会自动收集整个文件中所有级别的标题, 按级别构建目录树, 并为目录中每个标题建立指向对应位置的跳转链接. \
Insert a new line with `[TOC]` to establish table of contents. while TOC will collect all headings in current file of any levels, construct directory tree by level, and create jump links pointed to relative location for each heading in TOC. 

> [!NOTE]
> 注意: `[TOC]`在GitHub渲染器中不起作用. \
> Note: `[TOC]` does not function in GitHub renderer. 

***

# 链接 / Links

## 外部链接 / External Links

### 基本形式 / Basic Style
外部链接的基本形式为: 先用左右方括号括注链接名称, 紧随其后用左右圆括号括注链接的地址(不能以\#号打头, 不能包含空格), 二者间无分隔符. 即: \
Basic style of an external link is represented as the name of link wrapped by brackets, followed by target location (w/o leading "\#"s or whitespaces) wrapped by parentheses without seprator. id est. 
```markdown
[name-of-link](target-location)
```
例如: [点击这个链接会跳转到Markdown的基础语法介绍页面](https://www.markdownguide.org/basic-syntax/), 网址是`https://www.markdownguide.org/basic-syntax/`

### 链接的悬停工具提示 / Tooltips for Links on Hovering
如需为链接指定在鼠标悬停于其上期间的工具提示, 需在圆括号内, 链接地址的末尾, 以空格分隔, 后接以半角双引号括注的提示文本. 即: \
To assign tooltip text while hovering over the link, seperate tooltip text wrapped by quotes with a whitespace after the target location in parentheses. id est. 
```markdown
[name-of-link](target-location "tooltip-text")
```
例如: [点击这个链接会跳转到Markdown的扩展语法介绍页面](https://www.markdownguide.org/extended-syntax/ "https://www.markdownguide.org/extended-syntax/"), 网址可通过将鼠标悬停在链接上查看. 

## 内部链接 / Internal Links

> [!IMPORTANT]
> 本示例中对内部链接的定义, **基于Markdown语法的变形规则: `Github-Flavored Markdown(GFM)`.** \
> Definition of internal links in this example is **based on variation rules of Markdown grammar: `GitHub-Flavored Markdown(GFM)`.** 

### 内部链接的构造 / Construction of Internal Links
内部链接由两个部分组成: 链接入口和链接出口. \
Internal links consist of two parts: an entry and an exit. 

* 链接出口即为任意一级标题. \
    The exit of an internal link is a heading of any level.

* 链接入口的形式与外部链接相同, 但链接的地址以"\#"号打头, 后接链接出口的标题文本(**无空格**). 其中: \
    The format of entries is the same as external links, while the target location is led by a "#", instantly followed by caption of heading at the exit of link **w/o whitespaces**. 

    1. 标题中的拉丁字母全部替换为小写形式; \
        Latin letters in captions are replaced by lower case; 
        
    1. 标题中的空格全部替换为"连字符"; \
        Whitespaces in captions are replaced by hyphens; 
        
    1. 标题中除空格和"连字符"外的其他标点符号全部移除. \
        All punctuations, except whitespaces and hyphens, will be removed. 

例如, 点击以下链接将[回到本节的标题](#内部链接的构造--construction-of-internal-links), 该链接的目标地址被写作`#内部链接的构造--Construction-of-Internal-Links`

***

# 尾注 / Endnotes

## 尾注的结构 / Structure of Endnotes
尾注由两个部分组成: 尾注入口和尾注出口. \
Endnotes consist of two parts: an entry and an exit. 

尾注出口应当形成独立的段落. \
尾注入口可以插入至任何一级标题, 正文, 表格文本和任何一级引用块内, 但不能插入至代码块和 $L^AT_EX$ 公式块内. \
The exit of an endnote should form into a standlone paragraph. \
THe entry of an endnote can be inserted into headings of any levels, body texts, texts in grid lists, and reference blocks of any levels. \
Insertion of entries into code blocks and $L^AT_EX$ formulae is not available. 

尾注应具有文档内唯一的识别码, 识别码以单个"文本插入符"(\^)打头, 后接数字, 字母, 下划线或三者的组合. 其中: \
An endnote should contain a unique ID in current document. ID leads by a circumflex, followed by numerals, letters, underscores, or combinations of all above. 

* 一般不推荐使用纯数字组成的顺序码作为识别码. \
    Sequential combinations of pure numerals are not recommended in general. 

* 识别码中的字母**不区分**大小写. \
    Letters in IDs are **NOT** case-sensitive. 

## 尾注入口的构造 / Construction of Entry of Endnotes
在需要标注引用的位置插入尾注的入口, 需在插入点以方括号括注尾注的识别码. \
To insert the entry of an endnote into a place for citation, use brackets to wrap the ID of endnote. \
例如: 

> 天文信息学的诞生，立足于天文观测和数据处理工作中指数级增长的数据体量，和不能适应这一增长趋势的数据挖掘、分析能力之间的矛盾；立足于天文工作中跨学科交流、产学研融合项目对新方法论的需求[^DBOL_ArXiv_1612_06238]。它是天文学领域中，旨在解决以科学发现为用途的，多源数据、信息、知识资源的集成和挖掘问题[^DBOL_ArXiv_0909_3892]的学科分支。天文信息学的发展，必将在天文学界掀起一波方法论层面的浪潮[^DBOL_ArXiv_1201_1867]。

经渲染后, 尾注入口显示为上标状态下, 该引用在文档中首次出现的次序, 并被括注于方括号内. \
After rendering, the entry of endnotes display as orders of their appearance in current document in superscript form, wrapped by brackets. 

## 尾注出口的构造 / Construction of Exit of Endnotes
每个尾注出口应当形成独立的段落, 以方括号括注的尾注识别码开头, 后接一个冒号和一个半角空格, 其后是尾注的内容. \
The exit of an endnote should form into a standlone paragraph, beginning with ID wrapped by brackets, sequentially followed by a colon, a whitespace, and the content of endnote. \
例如: 
```markdown
[^DBOL_ArXiv_0909_3892]: BORNE K D. Astroinformatics: A 21st Century Approach to Astronomy[DB/OL]. (2009-09-22) [2023-05-21]. https://arxiv.org/abs/0909.3892
```

[^DBOL_ArXiv_0909_3892]: BORNE K D. Astroinformatics: A 21st Century Approach to Astronomy[DB/OL]. (2009-09-22) [2023-05-21]. https://arxiv.org/abs/0909.3892

尾注出口在脚本中的放置位置和顺序, 对其在渲染后的位置无影响. 经渲染后, 尾注的出口统一排版至文档末尾, 按照其入口在文档中首次出现的次序排序. \
The location of exits in Markdown scripts will not affect their location in rendered form. 

例如, [前文](#尾注出口的构造--Construction-of-Exit-of-Endnotes)中的第一个尾注出口并非位于脚本文件末尾, 且该尾注出口, 与以下两个尾注出口的排列顺序是按照Arχiv收录时间由早到晚排列, 但在当前文档中, 最先标引的是Arχiv文章`1612.06238`, 因此渲染后的结果中, 所有正文中间没有任何尾注, 尾注全部被排版至["参考文献"](#参考文献--References)这一标题之后, 而且排在最前的参考文献就对应地是Arχiv文章`1612.06238`: \
For example, the exit of first endnote [above](#尾注出口的构造--Construction-of-Exit-of-Endnotes) is not placed at the end of script file, meanwhile, this exit, along with exits of the following two endnotes, are sorted by the date of acceptance of respective articles in accending order. However, Arχiv article `1612.06238` is cited priorly in current document. Therefore, there is no endnote in the body text of rendered format. All endnotes are listed below the heading ["References"](#参考文献--References), while the first reference listed is exactly Arχiv article `1612.06238`: 

```markdown
[^DBOL_ArXiv_1201_1867]: BRESCIA M, LONGO G. Astroinformatics, data mining and the future of astronomical research[DB/OL]. (2012-01-09) [2023-07-10]. https://arxiv.org/abs/1201.1867

[^DBOL_ArXiv_1612_06238]: FEIGELSON E D. The changing landscape of astrostatistics and astroinformatics[DB/OL]. (2016-12-19) [2023-09-01]. https://arxiv.org/abs/1612.06238
```

[^DBOL_ArXiv_1201_1867]: BRESCIA M, LONGO G. Astroinformatics, data mining and the future of astronomical research[DB/OL]. (2012-01-09) [2023-07-10]. https://arxiv.org/abs/1201.1867

[^DBOL_ArXiv_1612_06238]: FEIGELSON E D. The changing landscape of astrostatistics and astroinformatics[DB/OL]. (2016-12-19) [2023-09-01]. https://arxiv.org/abs/1612.06238

***

# 参考文献 / References