N = int(input())
i = N // 5 
while True:
    if i < 0:
        print("-1")
        break
    if (N - 5 * i) % 3 == 0:
        five = i
        three = (N - 5 * i) // 3
        print(five + three)
        break
    else:
        i -= 1