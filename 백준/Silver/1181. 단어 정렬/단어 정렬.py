N = int(input())

word_lst = []
for _ in range(N):
    word = input()
    word_lst.append(word)
word_lst = list(set(word_lst))
word_lst.sort()
# len값으로 sort하려면 sort(key = len)이라고 해야 함
word_lst.sort(key = len)

for i in range(len(word_lst)):
    print(word_lst[i])