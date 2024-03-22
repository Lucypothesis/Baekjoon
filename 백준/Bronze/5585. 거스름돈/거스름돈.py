T = int(input())
change = 1000 - T
count = 0
for i in [500, 100, 50, 10, 5, 1]:
    count += change // i
    change %= i
print(count)