num = 5
spaces = num-1
for sv in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    spaces -=1
    for val in range(sv,0,-1):
        print(val,end=' ')
    print()
