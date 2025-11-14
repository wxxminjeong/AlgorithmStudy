N = int(input())

list_seq = list(map(int, input().split()))

max_index = 0
max_seq = list_seq[max_index]

is_mountain = "YES"

for i in range(len(list_seq)):
    if list_seq[i] >= max_seq:
        max_seq = list_seq[i]
        max_index = i

for a in range(len(list_seq)):
    if a == 0:
        pre = list_seq[a]
        continue

    elif a <= max_index:
        if list_seq[a] <= pre:
            is_mountain = "NO"
            break
        elif list_seq[a] > pre:
            pre = list_seq[a]

    elif a > max_index:
        if list_seq[a] >= pre:
            is_mountain = "NO"
            break
        elif list_seq[a] < pre:
            pre = list_seq[a]

print(is_mountain)
