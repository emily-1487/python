# 執行 for 迴圈
# 當迴圈正常結束時,
# 執行else區塊立面的程式

# for i in range(2, 6):
#     print(i)
# else:
#     print("迴圈正常結束")

# 執行 while 迴圈
# 當迴圈正常結束時,
# 執行else區塊立面的程式
# i = 2
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("迴圈正常結束")
# import time
# #輸入秒數
# second = int(input("請輸入秒數:"))
# #倒數計時
# for i in range(second, 0, -1):
#     print(i)
#     time.sleep(1)
# else:
#     print("時間到!")
# break=直接跳出目前的迴圈
# 若迴圈有使用else則無效
# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1
i = 1
for i in range(1, 6):
    if i == 3:
        break
    print(i)
