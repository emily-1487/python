# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
#     i += 1
# a = int(input("請輸入跳繩次數:"))
# for i in range(1, a + 1):
#     if i % 10 == 0:
#         print("休息一下")
#         continue
#     print("第" + str(i) + "次跳繩")
import random

# random.randrange(3)
# random.randrange(0, 10, 2)
# print(random.randrange(101))
#random.randrange(終止值)
# print(random.randint(1, 1487))
# print(random.randint(起始值,終止值,遞進值))
# import random as r

# print(r.randint(1, 10))
# print(r.randrange(1, 10))
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
