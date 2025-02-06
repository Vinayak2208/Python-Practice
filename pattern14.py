n = 6  
for row in range(1, n + 1):
    if row % 2 != 0:
        for val in range(row):
            if (val + 1) % 2 == 0:
                print(0, end=" ")
            else:
                print(1, end=" ")

    else:
        for val in range(row):
            print(val % 2, end=" ")
    print()
