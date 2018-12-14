#coding=utf-8
total = 366
#input("请输入：");
money = [100,50,10,5,2,1]

money100 = total/money[0]
temp=total%money[0]
money50 = temp/money[1] 
temp=temp%money[1]
money10 = temp/money[2] 
temp=temp%money[2]
money5 =  temp/money[3] 
temp=temp%money[3]
money2 =  temp/money[4] 
temp=temp%money[4]
money1 =  temp/money[5] 
temp=temp%money[5]
print("100CNY",money100,"50CNY",money50,"10CNY",money10,"5CNY",money5,"2CNY",money2,"1CNY",money1)