# `ArcPy`_`IdlPy`_Integration_Exercise

## 概述 / Overview

### 本项目的开发目的 / Aim of Development of This Repository

* 整理`Python 3.x`中的各种与地信, 遥感有关的常用库的使用方法和应用案例. \
    To summerize usages and appliances of common libraries in `Python 3.x` related to GIS/RS. \
    
* 整理`arcpy`模块(基于`ArcGIS Desktop`和`Python 2.x` 32位)在空间数据自动处理中的使用方法和应用案例. \
    To summerize usages and appliances of module `arcpy` (based on `ArcGIS Desktop` and `Python 2.x` 32-bit) in automation of spatial data processing. 
    
* 整理`idlpy`模块(基于`ENVI 5.x` / `IDL 8.x` 和 "Python to IDL Bridge")在`IDl`与`Python`对接, `ENVI`遥感数据处理与交互中的使用方法和应用案例. \
    To summarize usages and appliances of module `idlpy` (based on `ENVI 5.x` / `IDL 8.x` and "Python to IDL Bridge") in docking `IDL` with `Python`, and RS data processing and interaction in `ENVI`. 

* 将`arcpy`和`idlpy`嵌入至现有的`Python`交互式编辑器中, 以供集成使用, 并使用"笔记本式"文档管理代码块. \
    To embed `arcpy` and `idlpy` into existent interactive editor for Python for intergrated usage. Meanwhile, use notebook-style document for codeblock management. 

### 本项目主要涉及的`Python 3.x`内建库 / Built-in `Python 3.x` Libraries Mentioned in This Repository

* 基本数学运算库. \
    Libraries for fundermental mathematical operation. 
    * `math`, `cmath`
    * `decimal`, `fractions`
    * `statistics`, `random`
* 字符串和文本文件处理相关库. \
    Libraries for processing of character strings and text files. 
    * `string`, `re`
    * `sys`, `os`, `io`
* 与GIS/RS有关的可交换文本文件导入导出, 如`JSON`/`GeoJSON`, `XML`/`KML`. \
    Libraries for import and export of GIS/RS-related exchangable textual files, e.g. `JSON`/`GeoJSON`, `XML`/`KML`
    * `json`, `xml`
    
### 本项目主要涉及的第三方`Python`库 / Third-Party `Python` Libraries Mentioned in This Repository

* 数值计算, 符号计算库. \
    Libraries for numerical and symbolic computation. 
    * `numpy`
    * `sympy`
* 数学建模, 数据挖掘, 通用科学数据计算相关库. \
    Libraries for mathematical modeling, data mining and general scientific data computation. 
    * `scipy`
    * `pandas`
* `ArcGIS Desktop`的`Python 2.x`接口. \
    `Python 2.x` interface of `ArcGIS Desktop`. 
    * `arcpy`, `archook`
* `IDL` / `ENVI`的`Python 2.x`接口 (Python to IDL Bridge). \
    `Python 2.x` interface of `IDL` / `ENVI` (Python to IDL Bridge). 
    * `idlpy`
    
## 运行环境信息 / Information of Environment for Excution

### 系统和程序包环境 / Environment of System and Packages

|项目<br>Item|值<br>Value|
|:-:|:-|
|处理器架构<br>Architecture of processor|Intel x86-64|
|操作系统内核<br>OS kernel version|Windows NT 6.1.7601|
|`Conda`管理器版本<br>`Conda` package manager version|`conda 4.7.12` (`python 3.7.4`, `requests 2.22.0`)|
|`Anaconda`发行版<br>`Anaconda` system release version|`anaconda 2019.10`|
|`ArcGIS`发行版<br>`ArcGIS` release version|`ArcGIS Desktop 10.5`|
|`ENVI`发行版<br>`ENVI` release version|`ENVI 5.3`|