'''
判斷輸入成績的等第
使用者輸入成績
顯示使用者的等第
成績等第
A : 90 以上
B : 80 分到 89 分
C : 70 分到 79 分
D : 60 分到 69 分
E : 59 分以下
ex:
例如:使用者輸入成績50 顯示E。使用者輸入62則顯示D
'''
s=input("請輸入成績")
if s>="90":  
    print("你的等級為A")
elif s>="80"and<="89":
    print("你的等級為B")
elif s>="70"and<="79":
    print("你的等級為C")
elif s>="60"and<="69":
    print("你的等級為D")
else:
    s<="59":
    print("你的等級為E")