num = 5
for ev in range(num-1,-1,-1):
    for sp in range(ev):
        print(' ',end=' ')
    for val in range(num,ev,-1):
        print(val,end=' ')
    print()
