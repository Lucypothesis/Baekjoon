N = int(input())

lst = []
i = 666
while True:
    if len(lst) == N:
        break
    if '666' in str(i):
        lst.append(i)   
    i += 1

print(lst[-1])