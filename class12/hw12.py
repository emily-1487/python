'''
HW12:
輸入一組整數範圍，將範圍中的所有質數顯示於畫面上。
EX：
請輸入開始整數:10
請輸入結束整數:50
11
13
17
19
23
29
31
37
41
43
47
'''
a = int(input("請輸入開始整數:"))
s = int(input("請輸入結束整數:"))

for i in range(a, s):
    for j in range(int(i / 2 + 1)):
        print(j)
