#文件读入方法实现
import tkinter as tk
import time
import random
class App():
    def read(int):
        global line
        for j in range(int):
            line=f.readline()
            return(line)
    def __init__(self):
        
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()
        
    
    def update_clock(self):
        f=open("data4.txt")
        self.label.configure(text=read(6))
        self.root.after(1000, self.update_clock)

app=App()
temp = []  # 初始化列表
finish = []
for i in range(3):
    x = int(input("input a super please: "))  # 控制输入转为int
    y = int(input("input a time please: "))  # 控制输入转为int
    z = int(input("input a name: "))
    temp.append(x)  # 放入列表
    temp.append(y)  # 放入列表
    temp.append(z)
    finish.insert(i, temp[-3:])  # 只取列表最后两位
else:
    finish.sort(reverse=True)  # 排
while len(finish) > 0:
    # var1.set(finish[0][0])
    # var2.set(finish[1][0])
    # var3.set(finish[2][0])
    systemtime = 0
    systemtime = systemtime + 1
    # print('预计运行时间', finish[0][1])
    # time.sleep(1)
    # print('系统时间计时器', systemtime,'s')
    #print('进程已运行时间', supertime,'s')
    finish[0][1] = finish[0][1]-1

    with open("data4.txt","a+") as f:                                                   #设置文件对象
        for i in finish:                                                                 #对于双层列表中的数据
            i = str(i).strip('[').strip(']').replace(',','').replace('\'','')+'\n'  #将其中每一个列表规范化成字符串
            f.write(i)  
    if systemtime % 5 == 0:
        finish[0][0] = finish[0][0]-1
        if finish[0][0] == max(finish):
            continue
        else:

            # print("\033[0;43m%s\033[0m" % "转入就绪队列")
            finish.sort(reverse=True)
    if finish[0][1] == 0:
        # print("\033[0;31m%s\033[0m" % "进程结束")
        supertime = 0
        del finish[0]


   # 这时文字变量储存器
# def read():
#     N=1
#     global line
#     f=open("data4.txt")
#     for j in range(N):
#         line=f.readline()
#         N=N+3
#         var1.set("1")
#         time.sleep(1)
#         var1.set("2")
#         var1.set("3")
#         time.sleep(1)
#         var1.set("4")
# f.close()







