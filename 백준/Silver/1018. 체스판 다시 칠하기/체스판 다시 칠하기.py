N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]

W_lst = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
# B_lst = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
lst = []
for row in range(N-7):
    for column in range(M-7):
        w_count = 0
        b_count = 0
        for i in range(8):
            for j in range(8):
                if W_lst[i][j] != table[row + i][column + j]:
                    w_count += 1
                # W_lst하고 B_lst가 반대니까 B_lst 쓸 필요 없이 그냥 else 써도 됨 우와~
                else:
                    b_count += 1
        lst.append(min(w_count, b_count))
print(min(lst))

# 좀 잘 하는듯
