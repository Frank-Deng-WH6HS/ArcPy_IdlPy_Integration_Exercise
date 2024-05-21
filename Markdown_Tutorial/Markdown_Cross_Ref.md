Markdown语法示例: 交叉引用\
Samples of Markdown Syntax: Cross-Referencing

***

# 目录 / Table of Contents
在Markdown中建立目录, 需另起一行使用
```Markdown
[TOC]
```
建立. 此时, 目录会自动收集整个文件中所有级别的标题, 按级别构建目录树, 并为目录中每个标题建立指向对应位置的跳转链接. \
Insert a new line with following code to establish table of contents: 
```Markdown
[TOC]
```
while TOC will collect all headings in current file of any levels, construct directory tree by level, and create jump links pointed to relative location for each heading in TOC. 

***

# 链接 / Links

## 外部链接 / External Links

### 基本形式 / Basic Style
外部链接的基本形式为: 先用左右方括号括注链接名称, 紧随其后用左右圆括号括注链接的地址(不能以\#号打头, 不能包含空格), 二者间无分隔符. 即: \
Basic style of an external link is represented as the name of link wrapped by brackets, followed by target location (w/o leading "\#"s or spaces) wrapped by parentheses without seprator. id est. 
```markdown
[name-of-link](target-location)
```
例如: [点击这个链接会跳转到Markdown的基础语法介绍页面](https://www.markdownguide.org/basic-syntax/), 网址是`https://www.markdownguide.org/basic-syntax/`

### 链接的悬停工具提示 / Tooltips for Links on Hovering
如需为链接指定在鼠标悬停于其上期间的工具提示, 需在圆括号内, 链接地址的末尾, 以空格分隔, 后接以半角双引号括注的提示文本. 即: \
To assign tooltip text while hovering over the link, seperate tooltip text wrapped by quotes with a space after the target location in parentheses. id est. 
```markdown
[name-of-link](target-location "tooltip-text")
```
例如: [点击这个链接会跳转到Markdown的扩展语法介绍页面](https://www.markdownguide.org/extended-syntax/ "https://www.markdownguide.org/extended-syntax/"), 网址可通过将鼠标悬停在链接上查看. 

***

## 内部链接 / Internal Links

**本示例中对内部链接的定义, 基于Markdown语法的变形规则: `Github-Flavored Markdown(GFM)`. **

### 内部链接的构造 / Construction of Internal Links
内部链接由两个部分组成: 链接入口和链接出口. \
Internal links consist of two parts: the entry and the exit. 

* 链接出口即为任意一级标题. \
    An exit of an internal link is a heading of any level.

* 链接入口的形式与外部链接相同, 但链接的地址以"\#"号打头, 后接链接出口的标题文本. 其中: \
    The format of entries is the same as external links, while the target location is led by a "#", followed by caption of heading at the exit of link. 

    1. 标题中的拉丁字母全部替换为小写形式; \
        Latin letters in captions are replaced by lower case; 
        
    1. 标题中的空格全部替换为"连字符"; \
        Spaces in captions are replaced by hyphens; 
        
    1. 标题中除空格和"连字符"外的其他标点符号全部移除. \
        All punctuations, except spaces and hyphens, will be removed. 

例如, 点击以下链接将[回到本节的标题](#内部链接的构造--construction-of-internal-links), 该链接的目标地址被写作`#内部链接的构造--Construction-of-Internal-Links`

## 尾注 / Endnotes

### 尾注的结构 / Structure of Endnotes

尾注由两个部分组成: 尾注入口和尾注出口. \
Endnotes consist of two parts: the entry and the exit. 

尾注出口应当形成独立的段落. \
尾注入口可以插入至任何一级标题, 正文, 表格文本和任何一级引用块内, 但不能插入至代码块和 $L^AT_EX$ 公式块内. \
An exit of an endnote should form into a standlone paragraph. \
An entry of an endnote can be inserted into headings of any levels, body texts, texts in grid lists, and reference blocks of any levels. \
Insertion of entries into code blocks and $L^AT_EX$ formulae is not available. 
