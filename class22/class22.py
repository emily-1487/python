# a=eval("1+2")
# print(a)

# a=eval("a+b")
# print(a)
# import os
# a="/path/to/file.txt"
# if os.path.isfile(a):

# file=open("example.txt","r")
# content=file.read()
# print(content)
# file.close()

# r 讀檔案,檔案不存在  回報錯誤
# r+ 讀寫檔案,檔案不存在    回報錯誤
# w 寫檔案, 檔案不存在   創建檔案
# w+ 讀寫檔案,檔案不存在   創建檔案
# a 續寫檔案,檔案不存在   創建檔案
# a+ 續讀寫檔案,檔案不存在   創建檔案

# with open("example.txt","r")as file:
#     content=file.read()
#     print(content)

# fileName="test.txt"
# Mode="w"
# myFile=open(fileName,Mode)
# myFile.write("Hi\n")#"\"=換行
# myFile.write("How old are you?")
# myFile.close()

# fileName="test.txt"
# Mode="a"
# myFile=open(fileName,Mode)
# myFile.write("Hi\n")#"\"=換行
# myFile.write("My age is 18")
# myFile.close()

# path="D:/桌面/python/test.txt"
# f=open(path,"r")
# total=f.read()
# print(total)
# f.close

# import math
# x=3.5
# y=3
# math.fmod(x,y)
# math.fabs(x)
# math.floor(x)
# math.ceil(x)

# import datetime
# nn=datetime.datetime.now()
# print(nn)
# Date=datetime.date.today

