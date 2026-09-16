a = input()
a = list(a)
n = []
flag = True
for i in a:
    i = int(i)
    # print(i)
    
    if i==0 and flag:
        n.append(1)
        flag = False
    else: 
        n.append(i)
if flag:
    n[-1]=0
ans = 0
for i in n:
    ans = ans*2 + i
print(ans)

# Please write your code here.