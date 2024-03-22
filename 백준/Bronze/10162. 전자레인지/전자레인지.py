T = int(input())
list=[]
if T % 10 == 0:
    for i in [300,60,10]:
        list.append(T // i)
        T = T % i
    print(*list)
else:
    print("-1")