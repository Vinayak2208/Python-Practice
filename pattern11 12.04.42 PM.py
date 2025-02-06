num =  7
col = 1
spaces = num-1
for line in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(col):
        print(line,end=' ')
    print()
    spaces -=1
    col +=2
