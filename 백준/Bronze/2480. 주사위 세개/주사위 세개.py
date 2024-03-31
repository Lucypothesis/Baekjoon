lst = list(map(int, input().split()))
if len(set(lst)) == 1:
    print(10000 + 1000* lst[0])
elif len(set(lst)) == 2:
    if lst.count(lst[0]) == 2:
        print(1000 + 100 * lst[0])
    else:
        print(1000 + 100 * lst[1])
else:
    print(max(lst) * 100)