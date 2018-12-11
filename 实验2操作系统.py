import tkinter as tk
# class App():

#     def set():
#         print('123')
        
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("实验2")
#         # self.Spinbox = tk.Spinbox(textvariable="bbb",from_=0, to=10)
#         # self.Spinbox.pack()
#         self.Entry = tk.Entry(textvariable="aaa")
#         self.Entry.pack()
#         var = tk.StringVar()
#         self.R1 = tk.Radiobutton(text="最先适用法", variable=var, value=1, command= set)
#         self.R1.pack()
#         self.R2 = tk.Radiobutton(text="最佳适用法", variable=var, value=2, command= set)
#         self.R2.pack()
#         self.R3 = tk.Radiobutton(text="最坏适应法", variable=var, value=3, command= set)
#         self.R3.pack()
#         self.Button1 = tk.Button(text="分配空间", command = set)
#         self.Button1.pack()
#         self.Button2 = tk.Button(text="回收空间", command = set)
#         self.Button2.pack()
#         self.root.mainloop()
a = int(input("请输入内存条最大空间:"))
arr = ['0' for _ in range(a)]
def neicu():
    # arr = [i for i in range(16)]
    j = 0
    while 1:
        print ("内存占用:",arr)
        k = j
        n = input("请输入内存标号:")
        l = int(input("请输入内存大小:"))
        j=j+l
        # del arr[2]
        if j>a:
                print("从第",k,"插入") #首
                print("第",j,"结束") #尾
                print("创建失败，内存不足")
                
                return arr
        for i in range(k, j):
            arr[i]=n
            # arr.insert(i,1)

            
        else:
            continue

def huishou():
    n = input("请输入清理内存标号:")
    t = 0
    for i in range(a):
        if arr[i]==n:
            arr[i]='0'
        else:
            t=t+1
    else:
        print("内存占用:",arr)
        
def insert_find():
    #顺序插入
    # arr=['0', '0', '0', '4', '4', '4', '4', '5', '5', '5', '5', '5', '0', '0', '0', '0']
    t=0
    n = input("请输入进程名字:")
    l = int(input("请输入内存l:"))
    for i in range(a):
        t=0
        for j in range(l):
            if arr[i+j]=='0':
                t=t+1
                if t == l:
                    print("从第",i,"个插入")
                    print("在第",i+l,"个结束")
                    print("内存占用:",arr)
                    return 

def insert_find2():
    # 最佳插入
    t=0
    n = input("请输入进程名字:")
    l = int(input("请输入内存l:"))
    for i in range(a):
        t=0
        for j in range(l):
            if i+j>=a:
                print("溢出")
                return
            if arr[i+j]=='0':
                print("i",i)
                print("ij",i+j)
                t=t+1
                print("t",t)
                if t == l:
                    print("从第",i,"个插入")
                    print("在第",i+l,"个结束")
                    print("内存占用:",arr)
                    

neicu()
huishou()
insert_find()           

