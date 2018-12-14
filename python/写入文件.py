data =[ ['a','b','c'],['a','b','c'],['a','b','c']]
with open("data2.txt","w") as f:                                                   #设置文件对象
    for i in data:                                                                 #对于双层列表中的数据
        i = str(i).strip('[').strip(']').replace(',','').replace('\'','')+'\n'  #将其中每一个列表规范化成字符串
        f.write(i)                 