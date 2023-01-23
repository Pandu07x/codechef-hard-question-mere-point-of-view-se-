for i in range(int(input())):
    x,y,x1,y1,x2,y2=map(int,input().split())
    bas=[x,y]
    fir=[x1,y1]
    sec=[x2,y2]
    bas.sort()
    fir.sort()
    sec.sort()
    if bas==fir:
        print(1)
    elif bas==sec:
        print(2)
    else:
        print(0)
