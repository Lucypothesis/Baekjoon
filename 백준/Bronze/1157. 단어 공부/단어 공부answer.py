word = input().upper()
# set()함수 이렇게 쓰는 거임
s_lst = list(set(word))
count_word = []
for i in s_lst:
    count_word.append(word.count(i))
if count_word.count(max(count_word)) > 1:
    print("?")
else:
    index = count_word.index(max(count_word))
    print(s_lst[index])
