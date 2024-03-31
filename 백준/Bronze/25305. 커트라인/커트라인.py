N, k = map(int, input().split())
sc = list(map(int, input().split()))

sc.sort(reverse = True)
cutline = sc[k-1]
print(cutline)