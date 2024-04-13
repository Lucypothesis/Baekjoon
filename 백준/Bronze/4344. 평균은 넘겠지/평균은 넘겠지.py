C = int(input())

for _ in range(C):
    lst = list(map(int, input().split()))
    avg = sum(lst[1:]) / (len(lst) - 1)
    count = 0
    for i in lst[1:]:
        if i > avg:
            count += 1
    print(str(round(count / (len(lst) - 1) * 100,3))+'%')