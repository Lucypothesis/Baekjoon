A, B = map(int, input().split())

sml_lst = []
for i in range(1, min(A, B)+1):
    if A % i == 0 and B % i == 0:
        sml_lst.append(i)
print(max(sml_lst))
print(A * B // max(sml_lst))
# while문 쓸 때 꼭 변수 초기값 설정해주기!
# 이렇게 쓰면 N이 엄청 클 때 시간초과됨
# N = 1
# while True:
#     if N % A == 0 and N % B == 0:
#         break
#     N += 1
# print(N)