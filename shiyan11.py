# #coding=utf-8
# x=input("请输入优先级：")
# rawxlist=x.split("空格")#分割
# print(rawxlist)
# xlist=rawxlist.sort()#排序
# print(xlist)
# def pcb():
#     print('This is a function')
#     a = 1+21
#     print(a)
import os
import time
raw=[]
temp=[] #初始化列表
time =[]
finish=[]

for i in range(5):
    x = int(input("input a super please: "))#控制输入转为int
    y = int(input("input a time please: "))#控制输入转为int
    # raw.append(x)#放入列表备份
    temp.append(x)#放入列表
    temp.append(y)#放入列表
    finish[i]= temp
    
    # time.append(time)#放入列表

# super.sort(reverse = True)#排序
print('优先级排序为',super)#输出

print('优先运行优先级为',max(super),'的进程','执行时间为',time[a])


    if time[raw.index(super[0])]!= 0:
        print('运行第',raw.index(super[0])+1,'个进程')
        super[0]=super[0]-1
        time[raw.index(super[0])]=time[raw.index(super[0])]-1
        super.sort(reverse = True)#排序
        print(super)
    else:
        del super[raw.index(super[0])]
        print ('运行时间到了，删除',raw.index(super[0])+1)
        super.sort(reverse = True)#排序



# for i in range(5):
#     # super.insert(super[i]-1,super[i])
#     super=[super[0]-1,super[1]-1,super[2]-1,super[3]-1,super[4]-1]#输出
#     print(super)
#     os.system('pause')
