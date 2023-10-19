'''
hw15
請將hw13的作業升級
• 請將果汁新增到list並使用list完成之前的功能
juices_list = ["蘋果汁","柳橙汁","葡萄汁","系統關閉"]
'''
while True:
    L = ["1.蘋果汁", "2.柳橙汁", "3.葡萄汁", "4.系統關閉"]
    for i in range(len(L)):
        print(L[i])
    a = input("請輸入編號:")
    if a == "1":
        print("蘋果汁")
    elif a == "2":
        print("柳橙汁")
    elif a == "3":
        print("葡萄汁")
    elif a == "4":
        print("系統關閉")
        break
    else:
        print("沒有此果汁")