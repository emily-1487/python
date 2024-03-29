'''
你製作了一台飲料機！這台飲料機有四個按鈕，每個按鈕
都會給出不同的飲料：
蘋果汁 🍎🍎
柳橙汁 🍊🍊
葡萄汁 🍇🍇
系統關閉 🔴🔴
客人會按這些按鈕來選擇他們想要的飲料。
選擇後系統會告訴他們他們選了什麼飲料，但是，如果客人選擇了「系統關閉」，飲料機就會停止工作。
如果客人按錯了按鈕（也就是輸入了不正確的編號），你需要告訴他們「輸入錯誤查無此果汁，請重新輸入」。
'''


# while True:
#     print("1. 蘋果汁")
#     print("2. 柳橙汁")
#     print("3. 葡萄汁")
#     print("4. 系統關閉")
#     a = input("請輸入編號:")
#     if a == "1":
#         print("您點的商品是蘋果汁")
#     elif a == "2":
#         print("您點的商品是柳橙汁")
#     elif a == "3":
#         print("您點的商品是葡萄汁")
#     elif a == "4":
#         print("系統關閉")
#         break
#     else:
#         print("輸入錯誤查無此果汁，請重新輸入")
def make_drink(button):
    if button == 1:
        return "蘋果汁 🍎🍎"
    elif button == 2:
        return "柳橙汁 🍊🍊"
    elif button == 3:
        return "葡萄汁 🍇🍇"
    elif button == 4:
        return "系統關閉 🔴🔴"
    else:
        return "無效的按鈕"


while True:
    button = int(input("請選擇按鈕（1-4）："))
    if button == 4:
        print("關閉飲料機")
        break
    else:
        drink = make_drink(button)
        print("你選擇的飲料是：" + drink)