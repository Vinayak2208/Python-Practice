num = 5
spaces = num-1
for sv in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    spaces -=1
    for val in range(sv,num+1):
        print(val,end=' ')
    print()
