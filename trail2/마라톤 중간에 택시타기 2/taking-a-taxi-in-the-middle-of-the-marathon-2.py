n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

import sys
MIN = sys.maxsize
def md(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


for i in range(n):
    past_coord = points[0]
    dis = 0
    for j in range(1,n):
        if i==j:
            continue
        else:
            dis += md(past_coord,points[j])
            past_coord = points[j]
    # print(dis)
    if MIN>=dis:
        MIN=dis

print(MIN)