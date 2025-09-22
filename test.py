def GCF():
    GCF = (x,y)
    x= input("What is X?")
    y= input("What is y?")
    x=int(x)
    y=int(y)
    i=0-1
    for h in range(x):
        if (x%(h+1)) == 0 and (y%(h+1)) == 0:
            list2.append(h+1)
