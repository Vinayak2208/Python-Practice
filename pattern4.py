num =  7
stars = 1
spaces = num // 2 
for row in range(num):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    if row < num//2:
     spaces -=1
     stars +=1
    else:
        spaces +=1
        stars -=1
