T = int(input())

for i in range(1,T+1):
    N = int(input())
    quater = N // 25
    dime = (N % 25) // 10
    nickel = ((N % 25) % 10) // 5
    penny =((N % 25) % 10) % 5
    print(quater, dime, nickel, penny)