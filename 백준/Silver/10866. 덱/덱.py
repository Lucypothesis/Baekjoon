# deque 쓰는 이유: list에 비해 빠름 (deque는 O(1) list는 O(n))
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque()
for _ in range(N):
    a = input().split()
    # push_front
    if a[0] == 'push_front':
        deq.appendleft(a[1])
    # push_back
    if a[0] == 'push_back':
        deq.append(a[1])
    # pop_front
    if a[0] == 'pop_front':
        print(deq.popleft() if deq else -1)
    # pop_back
    if a[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    # size
    if a[0] == 'size':
        print(len(deq))
    # empty
    if a[0] == 'empty':
        print(0 if deq else 1)
    # front
    if a[0] == 'front':
        print( deq[0] if deq else -1)
    # back
    if a[0] == 'back':
        print( deq[-1] if deq else -1)