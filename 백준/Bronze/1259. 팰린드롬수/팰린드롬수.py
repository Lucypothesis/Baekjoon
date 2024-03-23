while True:
    N = input()
    # break문은 먼저 써줘야함
    if N == '0':
        break
    if N == N[::-1]:
        print('yes')
    else:
        print('no')
