# unpdf
## 这是一个基于Python破解 PDF编辑密码 的软件。  

### Windows操作系统  

**本项目使用 `Python` 编写，需要安装并配置好 `Python`，使用源代码前请使用以下 `pip` 命令安装 `pikepdf` 。**  

```powershell
pip install pikepdf
```  

### Linux  

**同理，使用源代码前请使用以下 `pip` 命令安装 `pikepdf` 。**  

```console
$ pip install pikepdf
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
$ sudo apt update
$ sudo apt install python3-tk
```  

****  

**注：目前只能破解编辑密码，无法破解查看密码。**  
