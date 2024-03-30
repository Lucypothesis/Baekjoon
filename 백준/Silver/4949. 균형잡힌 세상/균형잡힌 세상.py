def check(a):
    s = []
    for x in a:
        if x == "(":
            s.append(x)
        elif x == ")":
            if not s or s[-1] != '(':
                return 'no'
            else:
                s.pop()
        elif x == "[":
            s.append(x)
        elif x == "]":
            if not s or s[-1] != '[':
                return 'no'
            else:
                s.pop()
    if s:
        return 'no'
    return 'yes'

while True:
    a = input()
    if a == ".":
        break
    print(check(a))