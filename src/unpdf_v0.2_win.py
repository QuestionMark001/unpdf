import tkinter
from tkinter import filedialog
import pikepdf
import os

# Windows
print('请选择PDF文件。 Please choose PDF.\n')

# 打开一个文件选择对话框
root = tkinter.Tk()
root.withdraw() # 隐藏多余的窗口

# 选择文件路径
filePath = filedialog.askopenfilename()

# 用pikepdf破解，并以unlocked.pdf保存在当前程序所在路径下
pdf = pikepdf.open(filePath)
pdf.save('unloked.pdf')

print('解密完成。 Unloked done.')
os.system("pause") # 请按任意键继续. . .