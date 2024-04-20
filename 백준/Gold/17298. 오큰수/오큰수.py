import sys
input = sys.stdin.readline

N = int(input())
num_lst = list(map(int, input().split()))

index_lst = [0]
answer_lst = [-1] * N

for i in range(1,N):
    while index_lst and num_lst[index_lst[-1]] < num_lst[i]:
        answer_lst[index_lst.pop()] = num_lst[i]
    index_lst.append(i)
    # print(index_lst)
    # print(answer_lst)
    # print("-----")
print(' '.join(map(str,answer_lst)))

# 진짜 넘 어렵다.. 이런 거 처음에 어케 생각해냄?