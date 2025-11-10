num_year = int(input())

if (num_year%4 == 0 and num_year%100 != 0) or (num_year%4 == 0 and num_year%400 == 0):
    is_leap = 1
else:
    is_leap = 0

print(is_leap)
