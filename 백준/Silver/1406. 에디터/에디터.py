from collections import deque

front_lst = list(input())
back_lst = deque()

N = int(input())
for _ in range(N):
    c = input()
    if c == "L":
        if front_lst:
            back_lst.appendleft(front_lst.pop())
    elif c == "D":
        if back_lst:
            front_lst.append(back_lst.popleft())
    elif c == "B":
        if front_lst:
            front_lst.pop()
    else:
        front_lst.append(c[-1])

front = ''.join(front_lst)
back = ''.join(back_lst)
print(front+back)

# 미쳣다 첨에 이런거 어케 생각해냄? 