#!/usr/bin/python
# -*- coding: UTF-8 -*-
# GUI_barcode.py
# author:Han    2021/1/13

import tkinter as tk
import barcode
from barcode.writer import ImageWriter
from PIL import *
from PIL import ImageTk
from tkinter.filedialog import askdirectory
from tkinter import messagebox

def selectPath(var):
    # down函数中，修改下载地址使用；此处需要引入askdirectory模块
    path_ = askdirectory()
    var.set(path_+'/')


def download(ean, var, data, pic_type):
    # down函数中，用于下载条形码使用
    try:
        # 下载文件
        with open(str(var.get() + str(data)+ '.'+str(pic_type)), 'wb') as f:
            ean.write(f)
            f.close()
        # 下载成功后，提示下载成功
        messagebox.showinfo(title='下载成功',message='文件 '+ str(data)+ '.'+str(pic_type) +' 已成功下载至'+ str(var.get()))
    except:
        # 下载失败后，提示下载失败
        messagebox.showerror(title='下载失败',message='下载异常，请联系Mr.Han处理！！！')


def down(ean, data, pic_type):
    '''
    本模块主要用于将上个模块生成的图片下载下来；本模块主要包含两部分:
    其一是选定文件下载路径，可通过selectPath模块修改路径；其二是下载操作
    '''
    tk.Label(window, text='下载地址：').place(x=40,y=480)
    var = tk.StringVar()
    var.set('C:/Users/Administrator/Desktop/')
    
    # 下载地址栏
    e2 = tk.Entry(window, width=25, textvariable=var)
    e2.place(x=120, y=480)
    
    # 修改下载地址；由selectPath函数实现
    b2 = tk.Button(window, text='修改', bg='#169BD5', fg='white',
                   width=10, height=1, command=lambda:selectPath(var))
    b2.place(x=305, y=480)
    
    # 下载图片文件；由download函数实现，函数中实现了下载成功的提示；
    b3 = tk.Button(window, text='下载', bg='#169BD5', fg='white',
                   width=10, height=1, command=lambda:download(ean, var, data, pic_type))
    b3.place(x=120, y=510)


def creat_pic(data, var_barcode_type, var_pic_type):
    # 使用python-barcode生成条形码图片，并通过修改imgLabel，展示图片
    EAN = barcode.get_barcode_class(str(var_barcode_type))
    if str(var_pic_type) == 'png':
        try:
            ean = EAN(str(data), writer=ImageWriter())
        except:
            messagebox.showerror(title='请重新输入',message='仅支持232位，英文、数字及常用英文符号')
            return
    else:
        return '当前仅支持png格式图片'
    bar_photo = ImageTk.PhotoImage(ean.render())
    imgLabel.config(image=bar_photo)
    imgLabel.image = bar_photo
    # 执行后续下载导出图片模块
    down(ean, data, var_pic_type)


window = tk.Tk()
window.title('条形码生成工具')
window.geometry('400x600')

tk.Label(window, text='条码号：').place(x=40,y=20)
tk.Label(window, text='条码类型：').place(x=40,y=50)
tk.Label(window, text='图片格式：').place(x=40,y=80)

# 条码号输入框内容
e = tk.Entry(window, width=30)
e.place(x=120,y=20)

# 条形码类型单选样式
var_barcode_type = tk.StringVar()
var_barcode_type.set('code128')
r = tk.Radiobutton(window, text='Code-128', variable=var_barcode_type, value='code128')
r.place(x=120,y=50)

# 图片格式单选样式
var_pic_type = tk.StringVar()
var_pic_type.set('png')
r1 = tk.Radiobutton(window, text='PNG', variable=var_pic_type, value='png')
r1.place(x=120,y=80)
# r2 = tk.Radiobutton(window, text='JPG', variable=var_pic_type, value='jpg')
# r2.place(x=200,y=80)

b1 = tk.Button(window, text='生成预览图片', bg='#169BD5', fg='white',
               width=15, command=lambda:creat_pic(e.get(), var_barcode_type.get(), var_pic_type.get()))
b1.place(x=120, y=120)

imgLabel = tk.Label(window)
imgLabel.place(y=180)


window.mainloop()
