# d={1:"a",2:"b"}
# values=d.values()
# for value in values:
#     print(value)
# d={1:"a",2:"b"}
# items=d.items()
# for item in items:
#     print(item)
#     print(item[0],item[1])
# d={1:"a",2:"b"}
# items=d.items()
# for key, value in items:
#     print(key, value)
# food_first={"蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}
# for food,count in food_first.items():
#     if food=="果汁":
#         print(food+":"+str(count)+"杯")
#     else:
#         print(food+":"+str(count)+"杯")    
# 新增or修改元素
# book={}
# book["書名"]="海邊的卡夫卡"
# book["作者"]="春上春樹"
# book
food_first={"蛋糕":1,"三明治":10,"果汁":20,"薯條":15,"披薩":2}
food_first["冰淇淋"]=10
food_first["熱狗"]=20
food_first["果汁"]=25
for food,count in food_first.items():
    if food=="果汁":
        print(food+":"+str(count)+"杯")
    else:
        print(food+":"+str(count)+"份")