while True:
    N = input()
    if N == '0':
        break
    # print(N_lst)
    if N == N[::-1]:
        print('yes')
    else:
        print('no')