# `ArcPy`_`IdlPy`_Integration_Exercise

## 概述 / Overview

### 本项目的开发目的 / Aim of Development of This Repository

* 整理`Python 3.x`中的各种与地信, 遥感有关的常用库的使用方法和应用案例. \
    To summerize usages and appliances of common libraries in `Python 3.x` related to GIS/RS. 
    
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

### 配置`arcpy` `idlpy`集成环境 / Configure Integrated Environment of `arcpy` and `idlpy`

本项目通过`anaconda`环境管理器, 创建一个名为`arcpy_idlpy_x32`的子环境, 集成`arcpy`和`idlpy`以供二次开发使用. 上述二次开发接口对接的软件具有以下特征: \
This repository creates an environment named `arcpy_idlpy_x32` via `anaconda` environment manager, which intergrates `arcpy` and `idlpy` for secondary development. Softwares docked by interfaces above contains features as follow: 

* `ArcGIS Desktop 10.x`主软件可在32位或64位系统下运行, 但附带的`python`解释器为`python 2.x`版本, **仅包含32位版本**. \
    The master product of `ArcGIS Desktop 10.x` can run on 32-bit or 64-bit systems, while its `python` interpreter is `python 2.x`, containing 32-bit release only. 

* `ENVI 5.3`/`IDL 8.5`的`python`接口 (Python to IDL Bridge) 支持`python 2.x`/`3.x`, 同时提供32位和64位版本. \
    The `python` interface of `ENVI 5.3`/`IDL 8.5` (Python to IDL Bridge) supports `python 2.x`/`3.x`, providing both 32-bit and 64-bit releases. 

因此, 需要创建一个相对独立的, 32位的`python 2.x`环境, 用于运行解释器并调用相关程序包. \
Therefore, creation of a standlone 32-bit `python 2.x` environment to run interpreter and invoke relative packages is required. 

> [!IMPORTANT]
>
> 在执行后续操作前, 可能需要关闭反病毒软件和第三方防火墙软件, 因为上述软件可能会阻止`anaconda`从镜像源下载程序包. 
>
> Before execution of following operations, developers are supposed to disable anti-virus softwares and third-party firewalls, which may block `anaconda` from downloading packages from mirror websites. 

#### 确定`ArcGIS`及其`python`解释器安装路径 / Verify Installation Path of `ArcGIS` and Its `python` Interpreter

`ArcGIS Desktop 10.x`在Windows系统中安装时, 安装向导会在准备阶段分两步指定`ArcGIS`主软件, 及其`python`解释器的安装目录, 这两个目录可能不同. 因此, 需要将二者区分开来. 需要确定 **~~`ArcGIS`的~~`python`解释器**所在目录以完成后续操作. \
During installation of `ArcGIS Desktop 10.x` on Windows, installation wizard will assign directories of `ArcGIS` master product, and its `python` interpreter, in two steps separately. Directories above may be different and need to be distinguished. To archive further operations, developers are supposed to verify directory in which **the `python` interpreter of `ArcGIS`** locates. 

在`Anaconda prompt`命令行中, 将 **~~`ArcGIS`的~~`python`解释器**所在目录设置为临时变量. \
In `Anaconda prompt`, set a temporary variable to store the path of **the `python` interpreter of `ArcGIS`**. 

> [!NOTE]
> 本文档中以**绝对路径**表示的安装路径**仅供参考**. 请以开发用机上`python`解释器的实际安装路径为准. 
>
> In current document, installation paths represented as ABSOLUTE paths are FOR REFERENCE ONLY. Please consult installation path of `python` interpreter *de facto*. 

```bash
set pyarcgis=D:\python27\ArcGIS10.5
```

> [!IMPORTANT]
> 临时变量的值仅在**当前命令行会话**中有效, 命令行关闭后将被清理或者复原. 
>
> 执行上述命令后, 请勿关闭命令行界面, 以便在后续命令中继续使用临时变量. 后续操作均在**同一控制台**中执行. 
>
> Values of temporary variables are valid in CURRENT CLI SESSION ONLY and will be cleared or restored after closing the console. 
>
> After excuting command above, do NOT close CLI, so that variables can be reused in following commands. Further operations will be executed in THE SAME CONSOLE. 

#### 确定`anaconda`安装路径

在`Anaconda prompt`命令行中, 将`anaconda`安装目录设置为临时变量. \
In `Anaconda prompt`, set a temporary variable to store the installation path of `anaconda`. 

```bash
set anacon=D:\Anaconda3
```

#### 建立并初始化环境

1. 为建立新环境初始化`anaconda`系统参数. \
    Initialize parameters of `anaconda` for creation of new environment. 

```bash
set CONDA_FORCE_32BIT=1
conda clean -i
```

2. 建立并进入新环境`arcpy_idlpy_x32`. \
    Create and enter new environment `arcpy_idlpy_x32`. 

```bash
conda create -n arcpy_idlpy_x32 python==2.7.12 pip==8.1.1 wheel==0.29.0 -y
conda activate arcpy_idlpy_x32
```

3. 在新环境中配置与`ipython`有关的包. \
    Configure packages related to `ipython` in new environment. 

```bash
conda install notebook ipykernel numpy==1.9.3 six==1.10.0 tornado==4.5.3 -y
```

4. 将`ArcGIS`的`python`解释器使用的部分包链接到新环境下. 
    Link several packages used by `python` interpreter of `ArcGIS` to new environment. 
    
```bash
chdir /D %anacon%\envs\arcpy_idlpy_x32\Lib\site-packages
mklink /D scipy %pyarcgis%\Lib\site-packages\scipy
mklink /D pandas %pyarcgis%\Lib\site-packages\pandas
mklink /D sympy %pyarcgis%\Lib\site-packages\sympy
mklink /D matplotlib %pyarcgis%\Lib\site-packages\matplotlib
mklink /D pytz %pyarcgis%\Lib\site-packages\pytz
mklink pyparsing.py %pyarcgis%\Lib\site-packages\pyparsing.py
mklink pyparsing.pyc %pyarcgis%\Lib\site-packages\pyparsing.pycpytz
mklink cycler.py %pyarcgis%\Lib\site-packages\cycler.py
mklink cycler.pyc %pyarcgis%\Lib\site-packages\cycler.pyc
mklink Desktop10.5.pth %pyarcgis%\Lib\site-packages\Desktop10.5.pth
```

5. 将新环境注册为`ipython`内核, 以便与`base`环境下的`Jupyter notebook`一同使用. \
    Register new environment as an `ipython` kernel for use with `Jupyter notebook` in `base` environment. 

```bash
pip install backports.functools_lru_cache
ipython kernelspec install-self
conda deactivate
set CONDA_FORCE_32BIT=.
```
