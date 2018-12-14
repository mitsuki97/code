# import tkinter as tk
# import time
# a=[1,2,3]
# window = tk.Tk()
# window.title('BY ZHANGXUDONG')
# window.geometry('400x400')
# t1 = tk.StringVar()
# def handler():
#     t1.set(a[0])
#     time.sleep(1)
#     t1.set(a[1])
#     time.sleep(1)
#     t1.set(a[2])


# t1.set('春季里那个百花开')
# entry = tk.Entry(window, textvariable = t1).pack()
# btn = tk.Button(window, textvariable='123', command=handler) #textvariable设置原文本，command=handler是设置按钮要执行的代码
# btn.pack()
# window.mainloop()
import tkinter as tk
import time
import random


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = random.randint(0,10)
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()