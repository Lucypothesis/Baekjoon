n = int(input())

table = [[0] * 101 for _ in range(101)]
# print(table)

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            nx = x + i
            ny = y + j
            if table[nx][ny] == 0:
                table[nx][ny] = 1

count = 0
for row in table:
    count += row.count(1)
print(count)
# ㄹㅇ 좀 개뿌듯함. 이제 2차원배열 문제 감 잡은듯 ? 초딩 올림피아드 문제 맞춰놓고 뿌듯해하는 수준 ㅋ 하지만 뿌듯한걸 어째요ㅜ
