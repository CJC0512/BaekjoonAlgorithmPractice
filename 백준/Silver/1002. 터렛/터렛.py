import math

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 두 원의 중심 사이의 거리
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # 두 원이 일치하는 경우
    if d == 0 and r1 == r2:
        print(-1)
    # 외접 또는 내접하는 경우
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
    # 두 원이 서로 교차하는 경우
    elif abs(r1 - r2) < d < r1 + r2:
        print(2)
    # 교점이 없는 경우
    else:
        print(0)
