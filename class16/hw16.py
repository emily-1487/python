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
while True:
    print("1. 新增餐點到點餐清單")
    print("2. 從點餐清單中移除特定餐點")
    print("3. 查詢餐點在點餐清單中的位置")
    print("4. 退出點餐機")
    a = input("歡迎使用點餐機！請選擇您想要的功能(輸入數字)：")
    if a == '1':
        # 新增餐點到點餐清單的程式碼
        print("您選擇了新增餐點到點餐清單功能")
    elif a == '2':
        # 從點餐清單中移除特定餐點的程式碼
        print("您選擇了從點餐清單中移除特定餐點功能")
    elif a == '3':
        # 查詢餐點在點餐清單中的位置的程式碼
        print("您選擇了查詢餐點在點餐清單中的位置功能")
    elif a == '4':
        print("感謝您使用點餐機，祝您用餐愉快！")
        break
    else:
        print("請輸入有效的選項！")
