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
