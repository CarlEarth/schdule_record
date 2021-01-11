# Unicode string
from print_useful import info_in, info_add,time_table
from print_useful import activity_time,time_table
from datetime import datetime
now = datetime.now()
#date = datetime.date.today()
filename=("登記行程輸出"+str(now.strftime("%m"))+str(now.strftime("%d"))+".txt")
print(filename)
f = open(filename,'a',encoding="utf-8")
print("---------------------" , file=f)
#輸出Google 日曆
info_in("會議名稱",f)
number= input("1. 縣長行程 2.邀請函 3.Line 訊息 4.函 登行程 5.函 6.致詞稿, 7.開會通知單 : ")
type1=["縣長行程","邀請函","LINE 訊息","函 登行程","函","致詞稿","開會通知單"]
if (int(number)>6):
    property=1
else:
    property=0
location = input("輸入詳細地點: ")
print("地點:",location,file=f)
name = input("輸入承辦人的名字: ")
print("<%s> %s (%s%s登)" %(type1[int(number)-1],name,now.strftime("%m"),now.strftime("%d")), file=f)
info_add("聯絡人、頭銜及聯絡電話",f)
info_in("業務科長",f,True)
info_in("業務承辦",f,True)
sche= activity_time(property,f)
time_table(sche,f)
info_add("指導單位",f,True)
info_add("主辦單位",f,True)
info_add("協辦單位",f,True)
f.close()
