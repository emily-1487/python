'''
當使用者輸入數值時，程式不僅提示再大再小還需要提示縮小過後的輸入範圍
EX:
請輸入0~100的整數:50
再小一點
請輸入0~50的整數:25
再小一點
請輸入0~25的整數:15
再大一點
請輸入15~25的整數:30
再小一點
請輸入15~25的整數:10
再大一點
請輸入15~25的整數:20
再大一點
請輸入20~25的整數:23
再大一點
請輸入23~25的整數:24
恭喜猜中!
'''
import random

a = random.randint(1, 101)
s = 1
d = 100
while True:
    z = str(s)
    x = str(d)
    i = int(input("請輸入" + z + "~" + x + "的數:"))
    if i == a:
        print("恭喜猜中")
        break
    elif i > a:
        print("再小一點")
        if i > d:
            continue
        elif i < d:
            d = i
        continue
    elif i < a:
        print("再大一點")
        if i < s:
            continue
        elif i > s:
            s = i
