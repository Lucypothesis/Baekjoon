N = int(input())
for i in range(N):
    data = input()
    score = 0
    total_score = 0 # OOXXOXXOOO
    for j in range(len(data)):
        if data[j] == 'O':
            score += 1
        else:
            score = 0
        total_score += score
    print(total_score)