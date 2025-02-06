num =  4
col = 2*num-1
spaces = 0
for line in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end=' ')   
    for val in range(col):
        print(line,end=' ')
    print()
    spaces +=1
    col -=2
