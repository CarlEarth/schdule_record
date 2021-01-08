# Unicode string
def info_in(s,f, ps=False):
    test=1
    while(test==1):
        sentence=("請輸入"+s+"或enter鍵繼續: ")
        info= input(sentence)
        again=input("重來(r)或enter鍵繼續: ")
        if (again=="r"):
            test=1
        else:
            test=0
            if (info!=""):
                if (ps==True):
                    print("%s: %s" %(s,info),file=f)
                else:
                    print(info,file=f)

def info_add(s,f, ps=False):
    jump=0
    while(jump==0):
        test=1
        box=[]
        while(test==1):
            length=len(box)
            sentence=("請輸入"+s+"或enter鍵繼續: ")
            info=input(sentence)
            if (info!=""):
                box.append(info)
                test=1
            else:
                test=0
        
        again=input("重來(r)或enter鍵繼續: ")
        if (again=="r"):
            jump=0
        else:
            jump=1
            if (length!=0):
                if (ps==True):
                    print("%s: %s" %(s,box[0]),file=f)
                    for i in range(1,length):
                        print("          %s" %(box[i]),file=f)
                else:
                    for i in range(0,length):
                        print(box[i],file=f)
def time_table(test1,f, test2=1):
    #test1: Determine if execute the function
    #test2: Determine when to jump out the loop
    while(test1==1  and test2==1 ):
        print("輸入流程時間範例：")
        print("1200140015001600")
        #print("將輸入 12:00 - 14:00")
        #print("      14:00 - 15:00")
        #print("      15:00 - 16:00")
        print("總共三個時間行程。")
        scheduletime=input("請輸入流程時間: ")
        length= len(scheduletime)
        numschedule=int(length/4-1)
        if (length%4==0 and length > 0):
            test2=10
            again=input("重來(r)或任意鍵繼續")
            if (again=="r"):
                test2=1
        else:
            print("錯誤請重新輸入")
            test2=1
    i=0
    schedule_box=[]
    while(test1==1  and test2==10 ):
        print(len(schedule_box),numschedule)
        schedule=input("輸入流程內容")
        if (schedule != ""):
            schedule_box.append(schedule)
        if (len(schedule_box)==numschedule):
            test2=100
            again=input("重來(r)或任意鍵繼續")
            if (again=="r"):
                test2=10
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
