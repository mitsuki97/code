# class app():

    j = 67
    d = 0
    a = 67[98, 25, 63, 97, 56, 51, 55, 55, 6]
    a.insert(0, j)
    def FCFS():
        for i in range(1, 10):
            if i % 2 !=0:
                d = d+abs(a[i]-a[i-1])
            if i % 2 == 0:
                d = d+abs(a[i-1]-a[i])
            return d

    def SSTF():
        b=[67] #b为整理排序后序列
        for j in range(9):
            m = max(a)
            for i in range(0, 9):
                if i+1 >= len(a):
                    break
                if abs(a[0]-a[i+1]) < m:
                    m = abs(a[0]-a[i+1])
                    t = i+1  # 标号
            a[0] = a[t]  # 放置首位
            del a[t]
            b.append(a[0])
        print(b)
        for i in range(0, len(b)-1):
            d = d + abs(b[i]-b[i+1])



    def SCAN():
        pass:
    def CSCAN():
        pass:
    def NStepSCAM():
        pass:


#d = (98-67)+(98-25)+(63-25)+(97-63)+(97-56)+(56-51)+(55-51)+(55-55)+(55-6)
63,56,55,55,51,25,6,97,98
 #   FCFS，SSTF，SCAN，CSCAN和 NStepSCAN
