import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    # 입력 처리 (N과 K, 그리고 각 사람의 정보)
    # 예시 입력 구조에 맞춰 수정이 필요할 수 있습니다.
    N = int(data[0])
    K = int(data[1])
    
    people = []
    idx = 2
    for _ in range(N):
        x = int(data[idx])
        sign = data[idx+1]
        score = 2 if sign == 'H' else 1
        people.append((x, score))
        idx += 2

    # 1. 위치를 기준으로 정렬
    people.sort(key=lambda p: p[0])

    # 2. 투 포인터 및 슬라이딩 윈도우 적용
    max_score = 0
    current_score = 0
    left = 0

    for right in range(N):
        # 오른쪽 사람 추가
        current_score += people[right][1]
        
        # 구간 크기(x_right - x_left)가 K를 초과하면 왼쪽 포인터 이동
        while people[right][0] - people[left][0] > K:
            current_score -= people[left][1]
            left += 1
            
        # 최대 점수 갱신
        if current_score > max_score:
            max_score = current_score

    print(max_score)

if __name__ == '__main__':
    solve()