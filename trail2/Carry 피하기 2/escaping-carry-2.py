n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def check_carry(x, y, z):
    while x > 0 or y > 0 or z > 0:
        if (x % 10) + (y % 10) + (z % 10) >= 10:
            return True 
        x //= 10
        y //= 10
        z //= 10
        
    return False 
  


MAX = -1
for i in range(n):
    SUM = 0
    for j in range(i+1,n):
        for k in range(j+1,n):
            SUM = 0
            if not check_carry(arr[i], arr[j], arr[k]):
                SUM = arr[i]+arr[j]+arr[k]
                # print(SUM)
                MAX = max(SUM,MAX)         
print(MAX)