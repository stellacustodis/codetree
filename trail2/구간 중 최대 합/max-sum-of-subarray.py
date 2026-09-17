n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
MAX = 0
for i in range(n-k+1):
    sum_v = 0
    for j in range(i,i+k):
        sum_v += arr[j] 
    if sum_v > MAX:
        MAX = sum_v
print(MAX)