lst = [int(input()) for _ in range(5)]

lst.sort()
avg = sum(lst) // 5
mid = lst[2]

print(avg)
print(mid)