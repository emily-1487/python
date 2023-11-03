'''
請幫點餐機設計一個選單，當顧客
使用點餐機時，可以看到所有可以
選擇的功能，並告訴機器他們想做什麼。
歡迎使用點餐機！請選擇您想要的功能(輸入數字)：
1. 新增餐點到點餐清單
2. 從點餐清單中移除特定餐點
3. 查詢餐點在點餐清單中的位置
4. 退出點餐機
'''
A_list = []
while True:
    print("1. 新增餐點到點餐清單")
    print("2. 從點餐清單中移除特定餐點")
    print("3. 查詢餐點在點餐清單中的位置")
    print("4. 退出點餐機")
    a = input("歡迎使用點餐機！請選擇您想要的功能(輸入數字)：")
    if a == '1':
        # 新增餐點到點餐清單的程式碼
        print("您選擇了新增餐點到點餐清單功能")
        new_list = input("請輸入新的菜單")
        A_list.append(new_list)
        print("以新增餐點到點餐清單")
    elif a == '2':
        # 從點餐清單中移除特定餐點的程式碼
        print("您選擇了從點餐清單中移除特定餐點功能")
        number_list = input("輸入要移除的餐點:")
        if number_list in A_list:
            A_list.remove(number_list)
            print("已從點餐清單中移除特定餐點!")
        else:
            print("該餐點不再餐點清單中")
    elif a == '3':
        p = int(input("請輸入你想要插入的餐點:"))
        order = input("請輸入你想要加入的餐點:")
        A_list.insert(p, order)
        print("已在指定位置加入餐點!")
    elif a == '4':
        order = input("請輸入你想要計算的餐點:")
        count = A_list.count(order)
        print("餐點" + order + "在餐點清單中的數量是:" + str(count))
    elif a == "5":
        if A_list:
            A_list.pop()
            print("已取消點餐清單中的最後一項餐點!")
        else:
            print("點餐清單是空的!")
    elif a == "6":
        p = int(input("請輸入你想要取消的餐點位置:"))
        if 0 <= p < len(A_list):
            A_list.pop(p)
            print("已取消點餐清單中特定位置的餐點!")
        else:
            print("輸入位置不正確~")
    elif a == "7":
        A_list.sort()
        print("點餐出餐順序已按升序排序!")
    elif a == "8":
        A_list.sort(reverse=True)
        print("點餐出餐順序已按降序排序!")
    elif a == "9":
        A_list.reverse()
        print("點餐出餐順序已反轉!")
    elif a == "10":
        order = input("請輸入你想要查詢出餐順序的餐點")
        if order in new_list:
            index = new_list.index(order)
            print("餐點" + order + "出餐的順序是:" + str(index))
        else:
            print("該餐點不再清單中!")