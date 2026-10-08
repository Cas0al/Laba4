m=int(input())
d=int(input())
k=True
if not(1<=m<=12):
    k=False
if k:
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if not(1<=d<=31):
            k=False
    elif m==2:
        if not(1<=d<=28):
            k=False
    else:
        if not(1<=d<=30):
            k=False
if k:
    if m==1:
        print(365-d)
    elif m==2:
        print(334-d)
    elif m==3:
        print(306-d)
    elif m==4:
        print(275-d)
    elif m==5:
        print(245-d)
    elif m==6:
        print(214-d)
    elif m==7:
        print(184-d)
    elif m==8:
        print(153-d)
    elif m==9:
        print(122-d)
    elif m==10:
        print(92-d)
    elif m==11:
        print(61-d)
    elif m==12:
        print(31-d)
else:
    print(-1)
    
        
