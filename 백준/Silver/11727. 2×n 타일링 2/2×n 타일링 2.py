n = int(input())

def fc(n):
    a = 1
    for i in range(1,n+1):
        a *= i
    return a

def comb(n,k):
    return fc(n) // (fc(n-k) * fc(k))

answer = 0
k = n // 2
for a in range(k+1):
    answer +=  (2**a) * comb(n-a,a)
print(int(answer) % 10007)