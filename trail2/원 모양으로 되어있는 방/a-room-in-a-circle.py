n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.

import sys
MIN = sys.maxsize
for i in range(n):
    # print(a)
    cnt = 0
    for j in range(n):
        cnt+= (j)*a[j]
        # print(cnt)
    tmp = a[0]
    a.pop(0)
    a.append(tmp)
    # print(cnt)
    
    if MIN >= cnt:
        MIN = cnt

print(MIN)