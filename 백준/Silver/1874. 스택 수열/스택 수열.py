from collections import deque
n = int(input())
front_lst = []
back_lst = []
input_lst = []
plusminus_lst = []
num_lst = deque([i for i in range(1,n+1)])
for _ in range(n):
    x = int(input())
    input_lst.append(x) # [4,3,6,8,7,5,2,1]
    if num_lst and num_lst[0] <= x:
        for i in range(num_lst[0], x+1):
            front_lst.append(num_lst.popleft())
            plusminus_lst.append('+')
        back_lst.append(front_lst.pop())
        plusminus_lst.append('-')
    elif not num_lst or num_lst[0] > x:
        back_lst.append(front_lst.pop())
        plusminus_lst.append('-')

if back_lst != input_lst:
    print('NO')
else:
    for i in plusminus_lst:
        print(i)

# 미쳣다 내가 이걸 풀었다고?