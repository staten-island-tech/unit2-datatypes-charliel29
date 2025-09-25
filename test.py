def GCF():
    x = input("X?")
    y = input("Y?")
    x=int(x)
    y=int(y)
    list = []
    h=-1
    for i in range(x):
        if x%(i+1) == 0 and y%(i+1) == 0:
            list.append(i+1)
            h = h + 1
    print (list[h])
GCF()
