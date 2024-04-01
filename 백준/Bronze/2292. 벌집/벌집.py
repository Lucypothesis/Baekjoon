N = int(input())

i = 1
num = 1
while True:
    if num >= N:
        break
    num += 6 * i
    i += 1
print(i)