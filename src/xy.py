import tkinter as tk
import random
#處理複製功能
import pyperclip
#視窗參數設定###

win = tk.Tk()
win.title("Random x,y Generator")

#左上(0,0) 移動400 400
win.geometry("400x220+600+350")
win.config(bg="#323232")

#////////////////////////


def labelxy():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    x = str(random.randint(min_val,max_val))
    y = str(random.randint(min_val,max_val))
    xshow.config(text= "X:"+x)
    yshow.config(text= "Y:"+y)


#title
tit=tk.Label(bg="#323232",fg="skyblue",text="Random x,y Generator")
#obj.config(字形 大小)
tit.config(font="微軟正黑體 15")
tit.pack()

#min label
min_label=tk.Label(bg="#323232",fg="white",text="Min range")
min_label.pack()
#min ed
min_entry=tk.Entry()
min_entry.pack()

#Max label
max_label=tk.Label(bg="#323232",fg="white",text="Max range")
max_label.pack()
#max ed
max_entry=tk.Entry()
max_entry.pack()



#x label
xshow=tk.Label(bg="#323232",fg="white",text="")
xshow.pack()
#y label
yshow=tk.Label(bg="#323232",fg="white",text="")
yshow.pack()

#but Generate
butGen=tk.Button(text="Generate",command=labelxy)
butGen.pack()

#but Copy
btnCopy=tk.Button(text="Copy")
btnCopy.pack()



win.mainloop()