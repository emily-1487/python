# while=重複執行回圈內的敘述程式,直到判斷視為假
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1
# i = 0
# for i in range(5):
#     print(i)
#     i = i + 1
# += 加法
# -= 減法
# *= 乘法
# /= 小數除法
# //= 整數除法
# %= 取餘數
# **= 次方
# 優先順序:
# 1.() 括號
# 2.** 次方
# 3.+- 正負數
# 4.* / % // 乘 除 餘 取商
# 5.+- 加減法
# 6.== != > < >= <=
# 7.not and or
# 8.= += -= *= /= %= //= **=
# ans = ""
# while ans != "1234":
#     ans = input("請輸入密碼:")
#     if ans != "1234":
#         print("密碼錯誤,請重新輸入")
# print("歡迎光臨!")
# Sum = 0
# price = int(input("請輸入商品金額:"))
# while price != 0:
#     Sum += price
#     print("目前總金額為" + str(Sum) + "元")
#     price = int(input("請輸入商品金額:"))
x = int(input("請輸入正整數:"))
if x == 1:
    print(f"{x}不是質數")
else:
    i = 2
    while x % i != 0 and i != x:
        i += 1
    if i == x:
        print("yes")
    else:
        print("no")
