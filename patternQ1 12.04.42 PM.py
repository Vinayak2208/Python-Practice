num = 4
for row in range(1,5):
    for sp in range (num - row):
        print(' ',end = ' ')
    for col in range(row):
        print('*',end = ' ')
    print()
for row in range(1,4):
    for sp in range (row):
        print(' ',end = ' ')
    for col in range(num-row):
        print('*',end = ' ')
    print()
