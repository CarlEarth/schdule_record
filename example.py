# Unicode string
from print_useful import info_in, info_add,time_table
from datetime import datetime
now = datetime.now()
#date = datetime.date.today()
filename=("登記行程輸出"+str(now.strftime("%m"))+str(now.strftime("%d"))+".txt")
print(filename)
f = open(filename,'a',encoding="utf-8")
print("---------------------" , file=f)
#輸出Google 日曆
info_in("會議名稱",f)
number= input("1. 縣長行程 2.邀請函 3.Line 訊息 4.函 登行程 5.函 6.開會通知, 7.致詞稿 : ")
type1=["縣長行程","邀請函","LINE 訊息","函 登行程","函","開會通知","致詞稿"]
location = input("輸入詳細地點: ")
print("地點:",location,file=f)
name = input("輸入承辦人的名字: ")
print("<%s> %s (%s%s登)" %(type1[int(number)-1],name,now.strftime("%m"),now.strftime("%d")), file=f)
info_add("聯絡人、頭銜及聯絡電話",f)
info_in("業務科長",f,True)
info_in("業務承辦",f,True)
test,test1=1,1
#ttime=input("輸入開始結束時間，格式如 12001400 或1200: ")
xtt=0
while(xtt==0):
    ttime=input("輸入開始結束時間，格式如 12001400 或1200: ")
    if (len(ttime)==8):
        xtt=1
        print("活動時間 (%s:%s - %s:%s):" %(ttime[0:2],ttime[2:4],ttime[4:6],ttime[6:8]))
        change = input("不需要詳細流程?(y)或者任意鍵繼續")
        if (change=="y"):
            test,test1=0,0
            sche=0
            print("活動時間: %s:%s - %s:%s" %(ttime[0:2],ttime[2:4],ttime[4:6],ttime[6:8]),file=f)
        else:
            print("活動流程(%s:%s - %s:%s):" %(ttime[0:2],ttime[2:4],ttime[4:6],ttime[6:8]),file=f)
            sche=1
    elif (len(ttime)==4):
        xtt=1
        test,test1=0,0
        sche=0
        print("活動時間: %s:%s 開始" %(ttime[0:2],ttime[2:4]),file=f)
    else:
        xtt=0
        print("輸入錯誤｀請重新輸入")
time_table(sche,f)
info_add("指導單位",f,True)
info_add("主辦單位",f,True)
info_add("協辦單位",f,True)
f.close()
