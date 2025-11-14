N, M = map(int, input().split())  # N은 끊어진 기타줄의 개수 M은 기타줄 브랜드(메이커) 개수

list_guitar = []

for _ in range(M):
    list_guitar.append(list(map(int, input().split())))

effective_package = list_guitar[0][0]
effective_each = list_guitar[0][1]

# 효율좋은 패키지, 낱개 가격 탐색
for i in list_guitar:
    if i[0] < effective_package :
        effective_package = i[0]
    if i[1] < effective_each :
        effective_each = i[1]

if effective_package >= effective_each * 6:
    result = N * effective_each

elif (N // 6 + 1) * effective_package < (N//6) * effective_package + (N%6) * effective_each:
    result = (N // 6 + 1) * effective_package

else :
    result = (N//6) * effective_package + (N%6) * effective_each

print(result)
