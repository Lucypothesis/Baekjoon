def solution(n):
    lst = [0,1]
    for _ in range(99999):
        lst.append(lst[-1] + lst[-2])
    answer = lst[n] % 1234567
    return answer