word = input().upper() # MISSISSIPI
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(word)):
    index = alphabet.index(word[i])
    list[index] += 1

if list.count(max(list)) > 1:
    print("?")
else:
    print(alphabet[list.index(max(list))])