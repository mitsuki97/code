import time
import tkinter as tk
temp = []  # 初始化列表
finish = []
systemtime = 0
supertime = 0
for i in range(3):
    x = int(input("input a super please: "))  # 控制输入转为int
    y = int(input("input a time please: "))  # 控制输入转为int
    temp.append(x)  # 放入列表
    temp.append(y)  # 放入列表
    finish.insert(i, temp[-2:])  # 只取列表最后两位
else:
    finish.sort(reverse=True)  # 排序
while len(finish)>0:
    systemtime = systemtime + 1
    supertime = supertime + 1
    print('----------------')
    print('运行优先级为的程序', finish[0][0])
    print('预计运行时间', finish[0][1])
    time.sleep(1)
    print('系统时间计时器', systemtime,'s') 
    finish[0][1] = finish[0][1]-1
    if systemtime % 5 == 0:
        finish[0][0] = finish[0][0]-1 
        if finish[0][0]==max(finish):
            continue
        else:
            print("\033[0;43m%s\033[0m" % "转入就绪队列")
            finish.sort(reverse = True)
    if finish[0][1]==0: 
        print("\033[0;31m%s\033[0m" % "进程结束")
        supertime = 0
        del finish[0]

