# Unicode string
from print_useful import info_in, info_add
import datetime
date = datetime.date.today()
filename=("登記行程輸出"+str(date.month)+str(date.day)+".txt")
print(filename)
f = open(filename,'a',encoding="utf-8")
print("---------------------" , file=f)
#輸出Google 日曆
info_in("會議名稱",f)
number= input("1. 縣長行程 2.邀請函 3.Line 訊息 4.函 登行程 5.開會通知, 6.致詞稿 : ")
type1=["縣長行程","邀請函","LINE 訊息","函 登行程","函","開會通知","致詞稿"]
location = input("輸入詳細地點: ")
print("地點:",location,file=f)
name = input("輸入承辦人的名字: ")
print("<%s> %s (%s%s登)" %(type1[int(number)-1],name,date.month,date.day), file=f)
info_add("聯絡人、頭銜及聯絡電話",f)
info_in("業務科長",f,True)
info_in("業務承辦",f,True)
test,test1=1,1
print("若時間為12:00-14:00")
print("請輸入12001400")
ttime=input("輸入開始結束時間: ")
if (len(ttime)==8):
    print("活動時間 (%s:%s - %s:%s):" %(ttime[0:2],ttime[2:4],ttime[4:6],ttime[6:8]))
    change = input("不需要詳細流程?(y)或者任意鍵繼續")
    if (change=="y"):
        test,test1=0,0
        print("活動時間: %s:%s - %s:%s" %(ttime[0:2],ttime[2:4],ttime[4:6],ttime[6:8]),file=f)
    else:
        print("活動流程(%s:%s - %s:%s):" %(ttime[0:2],ttime[2:4],ttime[4:6],ttime[6:8]),file=f)
if (len(ttime)==4):
    test,test1=0,0
    print("活動時間: %s:%s 開始" %(ttime[0:2],ttime[2:4]),file=f)
test2=1
while(test2==1 and test1==1 ):
    print("範例：若時間為")
    print("12:00 - 1300")
    print("13:00 - 1400")
    print("14:00 - 1500")
    print("請輸入1200130014001500")
    scheduletime=input("輸入流程時間: ")
    length= len(scheduletime)
    numschedule=int(length/4-1)
    if (length%4==0):
        test2=0
    else:
        print("error, Please write it again")
        test2=1
i=0
schedule_box=[]
while(test==1):
    print("第%d個行程，共%d個",%(len(schedule_box)+1,numschedule))
    schedule=input("輸入流程內容")
    if (schedule != ""):
        schedule_box.append(schedule)
    if (len(schedule_box)==numschedule):
        test=0
        again=input("重來(y)或任意鍵繼續")
        if (again=="y"):
            test=1
            schedule_box=[]
            i=0
if (test1==1):
    time=scheduletime
    for j in range(0,numschedule):
        i=j*4
        print("%s:%s - %s:%s %s"
              %(time[i:i+2],time[i+2:i+4],
                time[i+4:i+6],time[i+6:i+8],schedule_box[j])
              ,file=f)
info_add("指導單位",f,True)
info_add("主辦單位",f,True)
info_add("協辦單位",f,True)
f.close()
