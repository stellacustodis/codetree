n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
c = []
coor = 0
for i in range(n):
    if d[i] == 'L':
        for j in range(t[i]):
            coor -= 1
            c.append(coor)
    else:
        for j in range(t[i]):
            coor += 1
            c.append(coor)

# B의 1초 마다의 위치 기록 (n 대신 m 사용)
c2 = []
coor = 0
for i in range(m):
    if d2[i] == 'L':
        for j in range(t2[i]):
            coor -= 1
            c2.append(coor)
    else:
        for j in range(t2[i]):
            coor += 1
            c2.append(coor)

ans = -1
for i in range(min(len(c), len(c2))):
    if c[i] == c2[i]:
        ans = i + 1  # 0번 인덱스는 1초를 의미하므로 i + 1
        break

print(ans)