#程序概要:
#  本程序包含五个主要方法，分别为:
#    - isvalid: 返回一个数字是否是合法的给定进制数
#    - convert: 返回转换后合适的字母或数字
#    - to_ten: 将任意进制数字转换为10进制数字
#    - ten_to: 将10进制数字转换为任意进制数字
#    - base_convert: 转换进制
#  另外的两个支持函数分别为:
#    - GUI: tkinter程序图像界面
#    - main: 实时获取用户输入并进行转换和输出
#  主要程序伪算法:
#    用户首先输入转换前数字，原进制与目标进制
#    接着，如果用户所输入的任一进制为10进制，则直接调用相应方法
#    如果两个进制皆不为10进制，则将原始数据先转换为10进制，然后再将返回值转换为目标进制
#  更新内容:
#    (17-5-9) 添加GUI
#    (17-5-9) 添加了判断用户输入的机制(检查是否为合法进制数)
#    (17-5-9) 使用了Python内置string模块

import tkinter as tk
from threading import Thread
from time import sleep
from string import digits
from string import ascii_uppercase as LETTERS

BASE_MAX = digits + LETTERS

def GUI():
    global root, numBox, fromBox, toBox, converted
    # Root
    root = tk.Tk()
    root.title('Base Converter')
    root.geometry('500x350')
    root.resizable(False, False)
    # Input boxes
    numBox = tk.Text(root, bd=0, font=('Menlo', 13))
    fromBox = tk.Text(root, bd=0, font=('Menlo', 13))
    toBox = tk.Text(root, bd=0, font=('Menlo', 13))
    fromBox.insert('end', '10')
    toBox.insert('end', '16')
    # Labels
    converted = tk.StringVar()
    result = tk.Label(root, textvariable=converted, font=('Menlo', 13))
    fromLabel = tk.Label(root, text='Original Base:', font=('Menlo', 13))
    toLabel = tk.Label(root, text='Target Base:', font=('Menlo', 13))
    numLabel = tk.Label(root, text='Number:', font=('Menlo', 13))
    # Placing Widgets
    fromLabel.place(x=40, y=50)
    toLabel.place(x=250, y=50)
    numLabel.place(x=40, y=150)
    fromBox.place(x=158, y=50, width=40, height=26)
    toBox.place(x=352, y=50, width=40, height=26)
    numBox.place(x=104, y=150, width=336, height=26)
    result.place(x=40, y=250)

def main():
    while True:
        try:
            num = numBox.get('0.0', 'end').upper().strip()
            fromBase = int(fromBox.get('0.0', 'end').upper().strip())
            toBase = int(toBox.get('0.0', 'end').upper().strip())
            converted.set('Converted: {}'.format(base_convert(num, fromBase, toBase)))
        except ValueError:
            converted.set('Converted: ERROR')
        sleep(0.05)

def base_convert(num, fromBase, toBase):
    if not ((2 <= fromBase <= 36 and 2 <= toBase <= 36) and isvalid(num, fromBase)):
        # return -1
        return 'ERROR'
    if fromBase == toBase:
        return num
    if fromBase == 10:
        return ten_to(int(num), toBase)
    elif toBase == 10:
        return to_ten(num, fromBase)
    else:
        return ten_to(to_ten(num, fromBase), toBase)

def isvalid(num, base):
    valid_digits = BASE_MAX[:base]
    return all([i in valid_digits for i in num])

def convert(num):
    num = str(num).upper()
    if len(num) > 1:
        return LETTERS[int(num)-10]
    elif num in LETTERS:
        return int(LETTERS.index(num)) + 10
    else:
        return int(num)

def to_ten(num, base):
    converted = 0
    for power, digit in enumerate(str(num)[::-1]):
        converted += convert(digit) * base ** power
    return converted

def ten_to(num, base):
    converted = ''
    while num >= base:
        remainder = convert(num % base)
        converted = str(remainder) + converted
        num //= base
    remainder = convert(num % base)
    return str(remainder) + converted

GUI()
try:
    Thread(target=main).start()
    root.mainloop()
except Exception:
    pass
