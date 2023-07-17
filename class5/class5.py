#  name = "python"
#  age = "31"
#  print("我叫做" + name + ",我今年" + age + "歲了")
# %+s=字串的變數
# %+d=整數的變數
# %+f=小數的變數
name = "python"
age = input("請輸入年齡")
age = int(age)
age = age + 10
print("我十年後是%d歲" % (age))