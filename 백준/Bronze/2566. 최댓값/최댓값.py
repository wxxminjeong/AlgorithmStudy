rows = 9

list_9x9 = [list(map(int, input().split())) for _ in range(rows)]

max_val = list_9x9[0][0]
col_num = 0
row_num = 0

for i in range(len(list_9x9)):
    for j in range(len(list_9x9[i])):
        if list_9x9[i][j] >= max_val:
            max_val = list_9x9[i][j]
            row_num = i + 1
            col_num = j + 1

print(max_val)
print(row_num, col_num)