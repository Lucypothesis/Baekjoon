import sys
from collections import deque

queue = deque()

input = sys.stdin.readline
n, k = map(int, input().split())

queue = deque(range(1, n+1))
# print(queue)

lst =[]
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    lst.append(queue.popleft())
print("<" + ', '.join(map(str, lst)) +">")