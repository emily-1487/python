# juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]
# print(juices_list)
# juices_list[0] = ["冬瓜茶"]
# print(juices_list)
# l = ["a,b,c"]
# print[l]
# l[0] = "A"
# print[l]
# a = ["晴天", "多雲", "雨天", "晴天","多雲", "雷陣雨", "晴天"]
# print(a)
# s = str(input("請輸入要修改得星期數字(1~7):"))
# a = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷陣雨", "晴天"]
# print(a)
# while True:
#     try:
#         s = int(input("請輸入要修改得星期數字(1~7):"))
#     except:
#         print("請輸入數字編號")
#     else:
#         if s > len(a) or s < 1:
#             print("查無資料!")
#         else:
#             print("你要修改得星期是" + str(s))
#             print("原本的天氣是" + a[s - 1])
#             x = input("請輸入新的天氣:")
#             a[s - 1] = x
#             print("修改後的天氣是" + a[s - 1])
#             print(a)
#             break
# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a)
# l = ["a", "b", "c"]
# a = l.copy()
# a[0] = 1
# print(a, l)
# [1,2]*2
# fruit_list = ["火龍果", "哈密瓜", "百香果", "橘子", "蘋果", "香蕉", "梨", "李", "桃"]
# print("最長的水果名字是" + max(fruit_list))
# print("最短的水果名字是" + min(fruit_list))
a = "2023/10/20"
a = a.split("/")
a = "-".join(a)
print(a)
