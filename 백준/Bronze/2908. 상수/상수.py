A, B = map(int, input().split())
A_lst = list(map(int, str(A)))
B_lst = list(map(int, str(B)))

# print(A) -> [7, 3, 4]
# print(B) -> [8, 9, 3]
for i in [2,1,0]:
    if A_lst[i] > B_lst[i]:
        print(int(''.join(map(str, A_lst[::-1]))))
        break
    elif A_lst[i] < B_lst[i]:
        print(int(''.join(map(str, B_lst[::-1]))))
        break