#coding=utf-8
name = ["张扬", "张旭东", "徐成", "刘一凡", "王美丽"]
cash = [1000, 2000, 1000, 1000, 1000]
social = ["无", "有", "无", "无", "无"]
#输出
count = 0
a = 0
while count < 5:
    if social[a] == "有":
        print("姓名:", name[a], "工资:", cash[a], "社保", social[a], "一共400元钱")
        count = count + 1
        a = a + 1
    else:
        print("姓名:", name[a], "工资:", cash[a], "社保", social[a])
        count = count + 1
        a = a + 1

