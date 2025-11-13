N, M = map(int, input().split())
card_list = list(map(int,input().split()))

gap = M  # M에서 세 카드의 합을 뺀 값

for i in range(N):  # N = len(card_list)
    if i + 2 >= N:
        break
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (M - (card_list[i] + card_list[j] + card_list[k]) < gap) and card_list[i] + card_list[j] + card_list[k] <= M:
                result = card_list[i] + card_list[j] + card_list[k]
                gap = M - (card_list[i] + card_list[j] + card_list[k])

print(result)
