<!--
 * @Author: QuestionMark001
 * @Date: 2022-02-19 08:04:03
 * @LastEditors: QuestionMark001
 * @LastEditTime: 2022-06-28 12:08:36
 * @FilePath: /LocalProjects/unpdf/README.md
 * @Description: 
 * 
 * Copyright (c) 2022 by QuestionMark001, All Rights Reserved. 
-->
# unpdf  

## 这是一个基于 Python 破解 PDF编辑密码 的软件  

### 本项目使用 `Python` 编写，需要事先安装并配置好 `Python` ，同时，请确保当前使用的 `Python` 版本号为 `3.0` 或 `3.0` 以上版本  

### Windows操作系统  

**使用源代码前请使用以下 `pip` 命令安装 `pikepdf` 。**  

```powershell
pip install pikepdf
```  

### Linux  

**同理，使用源代码前请使用以下 `pip` 命令安装 `pikepdf` 。**  

```console
pip install pikepdf
```  

**除此之外，直接运行源代码可能会提示 _`缺少tkinter模块`_ ：**  

```console
$ python unpdf_v0.2_linux.py
Traceback (most recent call last):
  File "/home/xyj/LocalProject/unpdf/src/unpdf_v0.2_linux.py", line 1, in <module>
    import tkinter
ModuleNotFoundError: No module named 'tkinter'
```  

**`deb` 系发行版可使用以下两行命令解决:**  

```console
sudo apt update
```

```console
sudo apt install python3-tk
```

**`arch` 系发行版可使用以下命令解决:**  

```console
sudo pacman -S tk
```

## 🍕如何使用  

**先切换到程序所在目录，然后使用以下命令：**  

**例如在 `Linux` 下使用 `unpdf v0.2版本` ：**  

```console
python unpdf_v0.2_linux.py
```

### 🎉使用例  

**🎈 本软件将打开一个tk窗口用来选择PDF文件，选择好PDF文件后，软件将会尝试破解该PDF文件的编辑密码（需要保证该PDF文件有且只有编辑密码，如有查看密码将会报错），由于是非暴力破解，基本可实现秒破，如图所示：**  

![Windows操作系统使用例](img/Windows使用例.gif "Windows操作系统使用例")  

**破解后的PDF文件将以 `unlocked.pdf` 保存在与 `unpdf` （即为本软件）相同的同级目录下。**  

****  

**注：目前只能破解只有编辑密码的PDF文件，无法破解查看密码。**  

## LICENSE  

****  

Apache License 2.0  
