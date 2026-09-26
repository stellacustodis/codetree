n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
c1, c2 = [0], [0]

for index, time in enumerate(t):
    for i in range(0,time):
        c1.append(c1[-1]+v[index])
for index, time in enumerate(t2):
    for i in range(0,time):
        c2.append(c2[-1]+v2[index])
# print(c1)
# print(c2)

MIN=min(len(c1),len(c2))
cnt = 0
LEADER = None
for i in range(MIN):
    # print(c1[i], c2[i])
    if c1[i]>c2[i]:  
        NEW_LEADER = 'A'
    elif c1[i]<c2[i]:
        NEW_LEADER='B'
    else:
        NEW_LEADER = LEADER 
    
    if LEADER is not None and LEADER!=NEW_LEADER:
        cnt+=1
    LEADER = NEW_LEADER
print(cnt)