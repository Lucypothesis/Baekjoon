import sys
import math
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    lst = deque(map(int, input().split()))
    # 10 10 10 10 20 10 / 5 25 5
    n = lst.popleft()
    answer = 0
    num_lst=[]
    for i in range(n):
        for j in range(n):
            if i < j:
                num_lst.append([i,j])
    # print(num_lst[2])
    # print(min([0,3]))
    for i in num_lst:
        a, b = lst[min(i)], lst[max(i)]
        # cd_lst = []
        # for i in range(1,a+1):
        #     if a % i == 0 and b % i == 0:
        #         cd_lst.append(i)
        # gcd = max(cd_lst)
        answer += math.gcd(a,b)
    print(answer)
# 오랜만에 풀었더니 이거 하나 푸는데 2시간이 걸렸다 미쳤다 아 -> 근데 시간초과 엔딩ㅋ
# -> import math 쓰면 시간 될까?