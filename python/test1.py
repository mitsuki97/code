import tkinter as tk
class App():
    def set():
        print('123')
        
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("实验2")
        # self.Spinbox = tk.Spinbox(textvariable="bbb",from_=0, to=10)
        # self.Spinbox.pack()
        self.Entry = tk.Entry(textvariable="aaa")
        self.Entry.pack()
        var = tk.StringVar()
        self.R1 = tk.Radiobutton(text="最先适用法", variable=var, value=1, command= set)
        self.R1.pack()
        self.R2 = tk.Radiobutton(text="最佳适用法", variable=var, value=2, command= set)
        self.R2.pack()
        self.R3 = tk.Radiobutton(text="最坏适应法", variable=var, value=3, command= set)
        self.R3.pack()
        self.Button1 = tk.Button(text="分配空间", command = set)
        self.Button1.pack()
        self.Button2 = tk.Button(text="回收空间", command = set)
        self.Button2.pack()
        self.root.mainloop()
app=App()