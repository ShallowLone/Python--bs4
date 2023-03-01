import tkinter as tk
import yf
import time 

def dl(): #下载的函数
    try:
        code = ent.get()
        df,name = yf.Y60s().get_dt(code)
    except:
        lbl['text'] = '下载失败!请检查' #下载失败
    else:
        df.to_csv('./Data.csv')
        lbl['text'] = name + '下载成功!'#下载成功
    
window = tk.Tk()
window.geometry('500x500')
window.title('雅虎港股股价下载器')
tk.Label(window, text = '欢迎使用雅虎港股股价下载器,请在下方输入您要查询的股票编号').pack()
ent = tk.Entry(window)
ent.pack()
tk.Button(window, text='开始下载', command = dl).pack()
lbl = tk.Label(window, width = 60, height = 10) 
lbl.pack()
window.mainloop()