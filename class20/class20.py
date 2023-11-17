# 鍵檢查=判斷字典裡有沒有key
#        如果有回傳True
#        如果沒有回傳False
# d={1:"a",2:"b"}
# print(1 in d)
# print("A" in d)
# print("a" in d)
# food_first={"蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}
# food_first["冰淇淋"]=10
# food_first["熱狗"]=20
# food_first["果汁"]=25
# present_food_list={"蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}
# for food,count in food_first.items():
#     if food=="果汁":
#         print(food+":"+str(count)+"杯")
#     else:
#         print(food+":"+str(count)+"份")
# print("還須購買的食物及數量")
# for food,count in food_first.items():
#     if not (food in present_food_list):
#         print(food+":"+str(count))
#     elif food in present_food_list and present_food_list[food]<count:
#         print(food+":"+str(count-present_food_list[food])
# pop=移除指定鍵的資料(必須存在)
#     返回被移除的資料值
# d={1:"a",2:"b"}
# v=d.pop(1)
# print("更新後的字典:",d)
# print("移除的數值:",v)
# pop 2=移除指定鍵的資料
#       如果鍵不存在,返回預設值
# d={1:"a",2:"b"}
# v=d.pop(100,"刪除資料失敗")
# print("更新後的字典:",d)
# print("移除的數值")
# food_first={"蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}
# food_first["冰淇淋"]=10
# food_first["熱狗"]=20
# food_first["果汁"]=25
# remaining_food={"蛋糕":0,"三明治":5,"果汁":8,"薯條":10,"披薩":1,"冰淇淋": 3, "熱狗": 0}
# # 更新食物列表並移除已經吃完的食物
# for food, count in remaining_food.items():
#     if count == 0:
#         food_first.pop(food, None)
#         print(food + "已經吃完")
#     else:
#         food_first[food] = count
# for food, count in food_first.items():
#     if food == "果汁":
#         print(food + ": " + str(count) + "杯")
#     else:
#         print(food + ": " + str(count) + "份")
# food_first={"蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}
# print(len(food_first))
# food_first["冰淇淋"]=10
# food_first["熱狗"]=20
# food_first["果汁"]=25
# print(len(food_first))
# len=取得key的數量
A={"小明":"樂高積木","小花":"畫筆","小強":"足球","小美":"書","小偉":"遙控車"}
print("一共收到了"+str(len(A))+"個禮物")
for name,A in A.items():
    print(name+"送了你一個"+A)