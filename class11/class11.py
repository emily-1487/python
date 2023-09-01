# 1+2+3+4...+100=梯形面積
# x = int(input("請輸入一個整數:"))
# Sum = 0
# for i in range(x + 1):
#     Sum = Sum + i
# Sum = str(Sum)
# x = str(x)
# print("從0加到" + x + "的總合為" + Sum)
# for i in range(1, 10):
#     a = 1 * i
#     i = str(i)
#     a = str(a)
#     print("1*" + i + "=" + a)
for i in range(1, 10):
    for j in range(1, 10):
        a = j * i
        i = str(i)
        j = str(j)
        a = str(a)
        print(j + "*" + i + "=" + a)
        j = int(j)
        i = int(i)
