
temp = []  # 初始化列表
finish = []
for i in range(3):
    x = int(input("input a super please: "))  # 控制输入转为int
    y = int(input("input a time please: "))  # 控制输入转为int
    # raw.append(x)#放入列表备份
    temp.append(x)  # 放入列表
    temp.append(y)  # 放入列表
    finish.insert(i, temp[-2:])  # 只取列表最后两位
    # time.append(time)#放入列表
else:
    finish.sort(reverse=True)  # 排序
    print('temp', temp)  # 源输出
    print('fin', finish)  # 格式整理输出

while len(finish)>0:
    print('运行优先级为的程序', finish[0][0])
        finish[0][0] = finish[0][0]-1
        finish[0][1] = finish[0][1]-1
        print('运行后时间剩', finish[0][1])
        if finish[0][1]==0: 
            del finish[0]
            
        print('运行顺序', finish)



