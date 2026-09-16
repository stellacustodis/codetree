R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]
# Please write your code here.

cnt = 0

color_s = grid[0][0]
color_e = grid[R-1][C-1]

if color_s == color_e:
    print(cnt)
else:
    for i in range(1,R-1):
        for j in range(1,C-1):
            for x in range(i+1,R-1):
                for y in range(j+1, C-1):
                    if grid[i][j]==color_e and grid[x][y]==color_s:
                        # print(i,j,x,y)
                        cnt+=1
    print(cnt)
    