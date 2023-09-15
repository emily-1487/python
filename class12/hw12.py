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
for i in range(a, s + 1):
    ans = False
    for j in range(2, int(i / 2 + 1)):
        if j != 1:
            if i % j == 0:
                ans = True
    if ans == False:
        print(str(i) + "是質數")

# if a ==1:
#     print("1不是質數")
# else:
#     for i in range(2,int(a/2+1)):
#         if a % i ==0:
#             ans = True
#     if ans == True:
#         print(str(a)+"不是質數")
#     else:
#         print(str(a)+"是質數")