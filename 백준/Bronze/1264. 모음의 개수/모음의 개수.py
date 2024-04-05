a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    count = 0
    lst = list(input())
    if '#' in lst:
        break
    for i in lst:
        if i in a:
            count += 1
    print(count)