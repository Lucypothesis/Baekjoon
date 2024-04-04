import sys
input = sys.stdin.readline

lst = list(input())

total = []
final = []
for i in range(len(lst)-1):
    # 막대기 등장~
    if lst[i] == '(' and lst[i+1] == '(':
        total.append(0)
    elif lst[i] == ')' and lst[i-1] == ')':
        final.append(total.pop() + 1)
    # 레이저 나올 때 있는 막대기 다 절단되니까 횟수 일괄 올리기
    elif lst[i] == '(' and lst[i+1] == ')':
        if total:
            for j in range(len(total)):
                total[j] += 1
# print(total)
# print(final)
# print(count)
print(sum(final)+ sum(total) + len(total))
# 이거 맞으면.. 눈물 흘림.. 기쁨의 눈물 ..