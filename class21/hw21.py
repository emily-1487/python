'''
製作一個丟骰子的指令
使用者可以輸入擲骰子的次數n
指令會一次回傳所有擲骰子的結果
程式內容前兩行打成
import random
def roll_dice(n):
'''
import random
def roll_dice(n):
    results=[]
    for _ in range(n):
        a=random.randint(1,6)
        results.append(a)
    return results
n=int(input("請輸入骰子的次數:"))
z=roll_dice(n)
print("擲骰子的結果：", z)
