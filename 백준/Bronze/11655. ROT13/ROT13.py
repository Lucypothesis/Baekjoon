S = input()
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def index_finder(case):
    rot13 = case.index(S[i]) + 13
    rot13 %= 26
    return case[rot13]

for i in range(len(S)):
    if S[i].isupper() == True:
        print(index_finder(upper), end ='')
    elif S[i].islower() == True:
        print(index_finder(lower), end ='')
    else:
        print(S[i], end ='')