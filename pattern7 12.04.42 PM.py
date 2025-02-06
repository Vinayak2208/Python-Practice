num = 5
spaces = num-1
for ev in range(2,num+2):
    for sp in range(spaces):
        print(' ',end=' ')
    spaces -=1
    for val in range(1, ev):
        print(val,end=' ')
    print()
