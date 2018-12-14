#文件读入方法实现
import tkinter as tk
import time
import random

class App():
    N1,N2,N3,N4,N5=1,2,3,4,5
    def __init__(self):
        
        self.root = tk.Tk()
        self.label1 = tk.Label(text="第一进程")
        self.label1.pack()
        self.label2 = tk.Label(text="第二进程")
        self.label2.pack()
        self.label3 = tk.Label(text="第三进程")
        self.label3.pack()
        self.label4 = tk.Label(text="第四进程")
        self.label4.pack()
        self.label5 = tk.Label(text="第五进程")
        self.label5.pack()
        self.Button = tk.Button(text="开始", command = self.update_clock)
        self.Button.pack()
        self.root.mainloop()
        
    
    def update_clock(self):
        global line1,line2,line3,line4,line5
        f=open("data5.txt")
        for j in range(1):
            line1=f.readline()
        for j in range(2):
            line2=f.readline()
        for j in range(3):
            line3=f.readline()
        for j in range(4):
            line4=f.readline()
        for j in range(5):
            line5=f.readline()  
        self.label1.configure(text=line1)
      
        self.root.after(3000, self.update_clock)
        App.N1=App.N1+5
        App.N2=App.N2+5
        App.N3=App.N3+5
        App.N4=App.N4+5
        App.N5=App.N5+5


app=App()
temp = []  # 初始化列表
finish = []
space=0
time = 0
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

    #print('运行优先级为的程序', finish[0][0])

    # print('预计运行时间', finish[0][1])
    
    #print('系统时间计时器', systemtime,'s')
    #print('进程已运行时间', supertime,'s')
    finish[0][1] = finish[0][1]-1
    time = time + 1
    with open("data4.txt","a+") as f:                                                   #设置文件对象
        f.write(('进程结束'+'\n')*space)
        for i in finish:                                                                 #对于双层列表中的数据
            i = str(i)+'\n'  #将其中每一个列表规范化成字符串
            f.write(i)  
    if time % 5 == 0:
        finish[0][0] = finish[0][0]-1   
        if finish[0][0]== max(finish)[0]:
            continue
        else:
                # with open("data4.txt","a+") as f:                                                   #设置文件对象                                                               #对于双层列表中的数据
                #     i = '转入就绪队列'  #将其中每一个列表规范化成字符串
                #     f.write(i)  
                # print("\033[0;43m%s\033[0m" % "转入就绪队列")
            finish.sort(reverse=True)
            time = 0
    if finish[0][1] == 0:         
        #print("\033[0;31m%s\033[0m" % "进程结束")
        time = 0
        del finish[0]
        space = space + 1
    else:
        continue
           
app=App()

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







