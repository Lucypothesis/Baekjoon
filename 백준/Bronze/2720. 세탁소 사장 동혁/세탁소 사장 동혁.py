T = int(input())
for _ in range(T):
    Money = int(input())
    amount_list = []
    for i in [25,10,5,1]:
        amount_list.append(Money // i)
        Money %= i
    print(*amount_list)