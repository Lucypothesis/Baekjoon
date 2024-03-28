N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
# print(lst)

for i in lst:
    count = 1
    for j in lst:
        if j[0] > i[0] and j[1] > i[1]:
            count += 1
    print(count)

# 와 좀 잘 풀었다 ㄹㅇ 좀 맘에 듦