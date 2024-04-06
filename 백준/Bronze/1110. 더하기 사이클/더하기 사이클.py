N = input()
if int(N) < 10:
    N_lst = list(N)
    N_lst.insert(0,'0')
    # print(N_lst)
else:
    N_lst = list(N)
count = 0
while True:
    num = N_lst[-1] + list(str(int(N_lst[0]) + int(N_lst[1])))[-1]
    count += 1
    N_lst = num
    if int(num) == int(N):
        break
print(count)
