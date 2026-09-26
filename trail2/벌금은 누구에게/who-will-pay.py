N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
n_list = [0]*(N+1)
n_flag = True
for s in student:
    n_list[s]+=1
    if n_list[s]>=K:
        print(s)
        n_flag = False
        break
if n_flag:
    print(-1)