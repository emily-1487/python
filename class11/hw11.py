"""作業1
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
hint:可以使用%取餘數進行判斷
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""
"""
作業2
請輸入要印出的箭頭大小
hint:
可利用字串乘法
>>>val="*" * 3
>>>print(val)
>>>***
EX:
請輸入要印出的箭頭大小:3
  *
 ***
*****
  *
  *
  *
"""
# hw11-1
a = int(input("請輸入正整數:"))
for a in range(1, a):
    b = a % 3
    c = a % 7
    if (b and c) == 0:
        print(a)
# hw11-2
a = int(input("請輸入箭頭大小:"))
for i in range(1, a + 1):
    print(' ' * (a - i) + '*' * (2 * i - 1))
for j in range(1, a + 1):
    print(' ' * (a - 1) + '*')