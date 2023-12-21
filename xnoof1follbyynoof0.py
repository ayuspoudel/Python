def ab(x,y):
    b1=0
    for i in range(x):
        b1 += 1
        if i<(x-1):
           b1 =  b1<<1
    for _ in range(y):
        b1 = b1<<1
    return b1
print(ab(5,2))
