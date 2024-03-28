from collections import deque
# 여기서는 sys.stdin.readline을 쓰나 안 쓰나 시간이 똑같이 걸림. sys.stdin.readline은 입력을 빠르게 받기 위해 사용하는데 입력이 1개밖에 없기 때문에 차이가 없는 거임! 
# import sys
# input = sys.stdin.readline
N = int(input())
q = deque(range(1,N+1))

for _ in range(N-1):
    q.popleft()
    q.append(q.popleft())
    
print(q[0])
