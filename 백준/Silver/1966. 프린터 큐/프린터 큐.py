import sys
from collections import deque
import math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    N , M = map(int, input().split())
    lst = deque(map(int, input().split()))
    lst[M] += 0.5
    ans_lst = []
    while lst:
        if math.floor(max(lst)) != math.floor(lst[0]):
            lst.append(lst.popleft())
        else:
            ans_lst.append(lst.popleft())
            if type(ans_lst[-1]) == float:
                print(len(ans_lst))
                break
                
# 이렇게 푸는 게 아닌 것 같지만 기발하긴 했다