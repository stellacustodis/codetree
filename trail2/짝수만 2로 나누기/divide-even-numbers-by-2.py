n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = []
for i in arr:
    if i%2==0:
        ans.append(i//2)
    else:
        ans.append(i)

print(*ans)