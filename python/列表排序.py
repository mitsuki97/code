a = [2,3,4,8,0,0,0,0]
b = [1,2,3,4,0,0,0,0]
c = []
for i in range(8):

    if a[i]<b[0]:
        c.append(a[i])
        del a[0]
    if a[i]==b[0]:
        c.append(a[i])
        c.append(a[i])
        del a[0]
    if a[i]>=b[0]:
        c.append(b[i])
        del b[0]
print(a)
print(b)
print(c)
   
   