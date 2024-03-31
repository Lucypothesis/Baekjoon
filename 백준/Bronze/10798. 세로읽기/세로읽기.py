table = [list(input()) for _ in range(5)]

# print(table)
for column in range(15):
    for row in range(5):
        if column < len(table[row]):   
            print(table[row][column], end = '')