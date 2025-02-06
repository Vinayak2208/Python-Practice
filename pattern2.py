num = 5
spaces = num // 2
for row in range(num//2 +1):
    for sp in range(spaces):
        print(' ',end = ' ')
    spaces -= 1
    for st in range(2*row + 1):
        print( '*',end = ' ')
    print()
spaces = 1
for row in range(num-2,0,-2):
    for sp in range(spaces):
        print(' ',end = ' ')
    spaces += 1
    for st in range(row):
        print( '*',end = ' ')
    print()
