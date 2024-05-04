num_lst = [] # 90
index_lst = []
for i in range(1,10):
    lst = list(map(int, input().split()))
    a = max(lst)
    num_lst.append(a)
    index_lst.append(lst.index(a))
x = max(num_lst)
row = num_lst.index(x)
print(x)
print(row+1, index_lst[row]+1)