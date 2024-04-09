from collections import deque
S = deque(list(input()))
# print(S) ['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n', ' ', 'o', 'n', 'l', 'i', 'n', 'e', ' ', 'j', 'u', 'd', 'g', 'e']
lst = []
lst2 = []
rvs_lst = deque()

while S:
    if S[0] == '<':
        while S:
            if S[0] == '>':
                lst.append(S.popleft())
                lst2 = []
                break
            else:
                lst.append(S.popleft())
        print(''.join(lst), end = '')
        lst = []
    else:
        while S:
            if S[0] == '<':
                rvs_lst.reverse()
                lst2.append(''.join(rvs_lst))
                rvs_lst = []
                break
            if S[0] == ' ':
                S.popleft()
                rvs_lst.reverse()
                lst2.append(''.join(rvs_lst))
                rvs_lst = []
            else:
                rvs_lst.append(S.popleft())
        else:
            rvs_lst.reverse()
            lst2.append(''.join(rvs_lst))
            rvs_lst = []
        print(' '.join(lst2), end = '')

# 점점 멋진 문제들을 잘 푸는듯.. 하하하