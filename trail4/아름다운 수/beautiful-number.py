n = int(input())

beautiful_count = 0

def count_beautiful_numbers(len_count):
    global beautiful_count

    if len_count == n:
        beautiful_count += 1
        return
    
    if len_count > n:
        return
    
    for i in range(1, 5):
        count_beautiful_numbers(len_count + i)

count_beautiful_numbers(0)
print(beautiful_count)