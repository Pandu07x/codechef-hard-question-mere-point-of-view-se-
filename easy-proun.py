for i in range(int(input())):
    x=int(input())
    p=input()
    a=list(p.strip())
    comm=0
    vo=0
    vol=["a","e","i","o","u"]
    for i in a:
        if i  in vol:
            comm=0
        else:
            comm+=1
        if comm==4:
            print("No")
            break
    if comm<4:
        print("Yes")
