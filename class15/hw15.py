'''
hw15
請將hw13的作業升級
• 請將果汁新增到list並使用list完成之前的功能
juices_list = ["蘋果汁","柳橙汁","葡萄汁","系統關閉"]
'''
while True:
    print(["1.蘋果汁", "2.柳橙汁", "3.葡萄汁", "4.系統關閉"])
    juices_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]
    a = input("請輸入編號:")
    if a == "1":
        print(juices_list[0])
    elif a == "2":
        print(juices_list[1])
    elif a == "3":
        print(juices_list[2])
    elif a == "4":
        print(juices_list[3])
        break
    else:
        print("沒有此果汁")
