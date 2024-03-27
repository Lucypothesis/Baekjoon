N = int(input())

lst = list(map(int, input().split()))

count = 0
for i in lst: # 3
    remain_lst = [i % n for n in range(1, i+1)]
    if remain_lst.count(0) == 2:
        count += 1

print(count)