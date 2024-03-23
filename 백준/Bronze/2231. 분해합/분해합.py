N = int(input())

def digit_total(x):
    sum = 0
    for i in range(6, -1, -1):
        digit = x // (10 ** i)
        x %= (10 ** i)
        sum += (10 ** i + 1) * digit
    return sum
    
lst=[]
for i in range(1,N+1):
    if digit_total(i) == N:
        lst.append(i)
# print(lst) -> [198, 207]
if len(lst) != 0:
    print(min(lst))
else:
    print("0")
    
# 어려웠는데 푸니까 ㄹㅇ 뿌듯함