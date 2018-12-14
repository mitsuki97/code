j = 67
d = 0
a = [98, 25, 63, 97, 56, 51, 55, 55, 6]
a.insert(0, j)
b=[67]
for j in range(9):
    m=max(a)

    for i in range(0,9):
        if i+1>=len(a):
            break
        if abs(a[0]-a[i+1])<m:
            m=abs(a[0]-a[i+1])
            t=i+1#标号
    a[0]=a[t] #放置首位
    del a[t]
    b.append(a[0])  
print(b)
for i in range(0,len(b)-1):
    d=d + abs(b[i]-b[i+1])
