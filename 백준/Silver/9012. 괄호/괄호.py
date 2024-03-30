def check(a):
    s = []
    for x in a:
        if x == "(":
            s.append(x)
        else:
            if not s or s[-1] == ')':
                return 'NO'
            else:
                s.pop()
    if s:
        return 'NO'
    return 'YES'
    
T = int(input())
for _ in range(T):
    a = input()
    print(check(a))
