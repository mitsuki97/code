import time
import tkinter
temp = []  # 初始化列表
finish = []
systemtime = 0
supertime = 0
for i in range(5):
    x = int(input("input a super please: "))  # 控制输入转为int
    y = int(input("input a time please: "))  # 控制输入转为int
    # raw.append(x)#放入列表备份
    temp.append(x)  # 放入列表
    temp.append(y)  # 放入列表
    finish.insert(i, temp[-2:])  # 只取列表最后两位
    # time.append(time)#放入列表
else:
    finish.sort(reverse=True)  # 排序
    #print('temp', temp)  # 源输出
    #print('fin', finish)  # 格式整理输出

while len(finish)>0:
    systemtime = systemtime + 1
    supertime = supertime + 1
    print('----------------')
    print('运行优先级为的程序', finish[0][0])
    print('预计运行时间', finish[0][1])
    time.sleep(1)
    print('系统时间计时器', systemtime,'s') 
    #print('进程已运行时间', supertime,'s') 
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

        
    #print('运行顺序', finish)



