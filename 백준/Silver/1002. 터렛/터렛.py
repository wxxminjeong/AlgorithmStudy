import math

def possible_coordinates(coordinates):

    x1, y1, r1, x2, y2, r2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5]
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 터렛 두개 사이 거리
    r_diff = abs(r1-r2)
    r_sum = r1+r2

    # 두 터렛의 위치가 같을 때(두 원의 중심이 일치)
    if d == 0:
        if r1 == r2:
            return -1
        elif r1 != r2:
            return 0

    # 교점 0개
    # 외부에서 만나지 않음, 내부에서 만나지 않음
    if r_sum < d or r_diff > d:
        return 0
    
    # 교점 1개
    # 외접, 내접
    elif r_sum == d or r_diff == d:
        return 1
    
    # 교점 2개
    # 서로 다른 두 점에서 만남
    elif d > r_diff and d < r_sum:
        return 2
    
T = int(input())

test_cases = []

for _ in range(T):
    test_cases.append(list(map(int,input().split())))

for case in test_cases:
    print(possible_coordinates(case))

# 하나하나 if 로 하려다 두 원의 위치 관계 수학적으로 이용하여 다시 만듬
# https://blog.naver.com/honeyeah/110140815554
# 두 원의 위치 관계

# def possible_coordinates(coordinates):

#     x1, y1, r1, x2, y2, r2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5]
#     r3 = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 터렛 두개 사이 거리

#     if x1==x2 and y1==y2 and r1==r2:  # 터렛 두개 위치가 같고 타겟 거리가 같으면 가능한 좌표 무한대
#         result = -1

#     elif x1==x2 and y1==y2 and r1!=r2:  # 터렛 두개 좌표가 같은데 거리가 다르면 가능한 좌표 0개
#         result = 0

#     elif r1 + r2 < r3:  # 관측거리의 합보다 두 터렛 사이의 거리가 더 멀면 가능한 좌표 0개
#         result = 0

#     elif r3 < r1 + r2:
#         result = 0

#     elif r1 + r2 == r3:  # 관측거리의 합과 두 터렛 사이 거리가 같으면 1개
#         result = 1

#     elif r2 == abs(r1 + r3):  # 내접
#         result = 1

#     elif r1 + r2 > r3:  # 관측거리의 합이 두 터렛 사이 거리보다 작으면 2개
#         result = 2

#     return result