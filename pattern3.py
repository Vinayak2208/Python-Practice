num =  5
stars = 1
for row in range(num):
    for st in range(stars):
        print('*',end=' ')
    print()
    if row < num//2:
     stars +=1
    else:
        stars -=1
