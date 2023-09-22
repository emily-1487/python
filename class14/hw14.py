import random

s = random.randrange(1, 100)
while True:
    a = int(input("請輸入1~100的整數:"))
    if a == s:
        print("恭喜答對!")
        break
    elif a < s:
        print("在大一點")
    elif a > s:
        print("在小一點")