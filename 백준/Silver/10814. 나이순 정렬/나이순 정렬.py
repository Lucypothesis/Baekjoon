import sys
input = sys.stdin.readline

N = int(input())

lst = [list(input().split()) for _ in range(N)]
# str과 int의 정렬: 20, 200, 21에서 str정렬은 20, 200, 21 순으로 정렬됨. 20, 21, 200 순으로 정렬하려면 int로 변환해줘야 함. 신경쓰기 ! 
lst.sort(key = lambda x : int(x[0]))

for i in lst:
    print(i[0], i[1])
