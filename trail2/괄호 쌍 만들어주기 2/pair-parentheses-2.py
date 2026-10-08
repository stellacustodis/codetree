A = input()

# Please write your code here.
cnt = 0
for i in range(len(A)-1):
    for j in range(len(A)-1):
        if A[i]==A[i+1] and A[i] == '(' and A[j]==A[j+1] and A[j]==')' and i+2<=j:
            cnt+=1
print(cnt)