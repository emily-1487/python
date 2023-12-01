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
    for i in range(n):
        results.append(random.randint(1,6))
    return results
z=int(input("請輸入骰子的次數:"))
print(roll_dice(z))