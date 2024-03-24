S = list(map(int, input()))
# print(S)
new_S = []
for i in range(len(S)-1):
    # 인덱스 i+1 쓸 때 범위 잘 확인하자
    # 냅다 쓰기만 하지 말고 결과 어떻게 나올지 머리를 굴리자ㅜ
    if S[i] != S[i+1]:
        new_S.append(S[i])
new_S.append(S[-1])

# print(new_S)
answer = min(new_S.count(0), new_S.count(1))
print(answer)