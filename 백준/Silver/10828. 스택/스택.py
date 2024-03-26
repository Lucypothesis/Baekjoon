# 이 상황에서 꼭 sys를 써야하는가? -> Yes. 안 쓰고 Python3으로 돌려봤더니 시간초과 뜸
import sys
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    stack = input().split()
    if stack[0] == 'push':
        lst.append(stack[1])
    elif stack[0] == 'pop':
        # 형식 이렇게도 쓸 수 있구나 생각해보기
        print(lst.pop() if lst else -1)
        # if len(lst) != 0:
        #    print(lst.pop())
        # else:
        #    print(-1)
    elif stack[0] == 'size':
        print(len(lst))
    elif stack[0] == 'empty':
        print(0 if lst else 1)
    else:
        print(lst[-1] if lst else -1)
