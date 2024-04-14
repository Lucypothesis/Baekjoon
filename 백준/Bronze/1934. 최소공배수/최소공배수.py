import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    lst = []
    for i in range(1, min(A,B)+1):
        if A % i == 0 and B % i == 0:
            lst.append(i)
    gcd = max(lst)
    lcm = A * B // gcd
    print(lcm)