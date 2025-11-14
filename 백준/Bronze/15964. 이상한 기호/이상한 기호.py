def atsign(A,B):
    return (A + B) * (A - B)

A, B = map(int, input().split())

print(atsign(A, B))