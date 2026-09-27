abilities = list(map(int, input().split()))

# Please write your code here.
# print(abilities)
max_sum = sum(abilities)
MIN = 10000000000

for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            c_sum = abilities[i]+abilities[j]+abilities[k]
            if MIN > abs(c_sum - (max_sum - c_sum)):
                MIN = abs(c_sum - (max_sum - c_sum))
print(MIN)