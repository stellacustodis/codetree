x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

coor = [[0] * 2001 for _ in range(2001)]
OFFSET = 1000

# 1. 첫 번째 직사각형 1로 채우기 (면적 기준이므로 +1 제거)
for i in range(OFFSET + x1[0], OFFSET + x2[0]):
    for j in range(OFFSET + y1[0], OFFSET + y2[0]):
        coor[i][j] = 1

# 2. 두 번째 직사각형 부분 0으로 지우기 (+1 제거)
for i in range(OFFSET + x1[1], OFFSET + x2[1]):
    for j in range(OFFSET + y1[1], OFFSET + y2[1]):
        coor[i][j] = 0

# 3. 잔해물을 덮는 최소 직사각형 경계(Bounding Box) 찾기
min_x, max_x = 2001, 0
min_y, max_y = 2001, 0
is_remaining = False

for i in range(2001):
    for j in range(2001):
        if coor[i][j] == 1:
            is_remaining = True
            if i < min_x: min_x = i
            if i > max_x: max_x = i
            if j < min_y: min_y = j
            if j > max_y: max_y = j

# 4. 넓이 계산 후 출력
if not is_remaining:
    # 1이 하나도 안 남아있으면 덮을 필요가 없으므로 넓이 0
    print(0)
else:
    # 배열의 인덱스 하나는 1x1 칸을 의미하므로 가로/세로 길이는 (max - min + 1)
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
    print(area)