S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lst = [0] * 26
for i in range(26):
    for k in S:
        if k == alphabet[i]:
            lst[i] += 1

for i in lst:
    print(i, end=' ')