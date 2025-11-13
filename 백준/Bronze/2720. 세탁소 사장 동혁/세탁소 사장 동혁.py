T = int(input())

list_C = []  # change 거스름돈

for _ in range(T):
    list_C.append(int(input()))

for C in list_C:
    Q = C // 25
    C = C % 25
    D = C // 10
    C = C % 10
    N = C // 5
    C = C % 5
    P = C // 1

    print(Q, D, N, P)
    