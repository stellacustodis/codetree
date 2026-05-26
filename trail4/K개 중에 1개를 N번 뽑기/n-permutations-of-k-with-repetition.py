K, N = map(int, input().split())

answer = []

def find_sequences(depth):
    if depth == N:
        print(*answer) 
        return

    for i in range(1, K + 1):
        answer.append(i)      
        find_sequences(depth + 1) 
        answer.pop()          
find_sequences(0)