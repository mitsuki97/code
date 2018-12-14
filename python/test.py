# a = [1,0,0,4,5,6,7,8,9,0]

# n = 3
# c= [a[i:i+n] for i in range(0, len(a), n)]
# print(c)

import itertools
a =['0', '0', '0', '4', '4', '4', '4', '5', '5', '5', '5', '5', '0', '0', '0', '0']
def maxL():
    b=[]
    for k,v in itertools.groupby(a):
        if k=='0':
            t=len(list(v))
            b.append(t)
            
        else:
            continue
    print("max",max(b))
maxL()