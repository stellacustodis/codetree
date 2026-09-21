n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
MAX_LEN = 0

for i in range(n):
    cnt = 0
    for j in range(i,n):
        # print(cnt)
        if arr[j]>t:
            # print(cnt)
            cnt+=1
            if cnt>MAX_LEN:
                MAX_LEN = cnt
        else:

            cnt = 0

print(MAX_LEN)