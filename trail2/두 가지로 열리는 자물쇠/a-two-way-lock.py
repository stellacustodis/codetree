N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
def get_dist(p1, p2, N):
    diff = abs(p1 - p2)
    return min(diff, N - diff)

def calculate(N, a, b, c, x, y, z):
    if get_dist(a, x, N) <= 2 and get_dist(b, y, N) <= 2 and get_dist(c, z, N) <= 2:
        return True
    return False
cnt = 0
for i in range(1, N+1):
    for j in range(1,N+1):
        for k in range(1, N+1):
            if calculate(N,a1,b1,c1,i,j,k) or calculate(N,a2,b2,c2,i,j,k):
                cnt+=1
print(cnt)