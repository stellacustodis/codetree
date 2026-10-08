n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max = 0

for i in range(n):
    sum_value = 0
    for j in range(n):
        if abs(i-j)>=2:
            sum_value = numbers[i] + numbers[j]
        if sum_value>=max:
            max = sum_value
print(max)