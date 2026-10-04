import sys
from itertools import permutations

# 1. 스트라이크(1번 카운트)와 볼(2번 카운트)을 계산하는 함수
def check_counts(candidate, guess):
    strike = 0
    ball = 0
    
    for i in range(3):
        # 자리가 같고 숫자도 같으면 스트라이크
        if candidate[i] == guess[i]:
            strike += 1
        # 자리는 다르지만 숫자가 포함되어 있으면 볼
        elif guess[i] in candidate:
            ball += 1
            
    return strike, ball

def main():
    input = sys.stdin.readline
    
    # 2. 질문의 개수 N 입력
    N = int(input())
    
    # B가 질문한 정보들을 리스트에 저장
    # 문자열 형태의 숫자, 스트라이크(정수), 볼(정수)로 튜플 형태로 묶어 저장
    questions = []
    for _ in range(N):
        num, s, b = input().split()
        questions.append((num, int(s), int(b)))
        
    # 3. 1~9로 만들 수 있는 서로 다른 세 자리 숫자 후보군(504개) 생성
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    candidates = ["".join(p) for p in permutations(digits, 3)]
    
    # 정답이 될 수 있는 숫자의 개수를 셀 변수
    possible_answer_count = 0
    
    # 4. 모든 후보군(504개)을 순회하며 검증
    for candidate in candidates:
        is_possible = True
        
        # 주어진 N개의 조건(B의 질문)과 모두 일치하는지 확인
        for guess_num, expected_s, expected_b in questions:
            s, b = check_counts(candidate, guess_num)
            
            # 단 하나라도 조건과 다르면 정답이 될 수 없으므로 중단
            if s != expected_s or b != expected_b:
                is_possible = False
                break
        
        # N개의 질문 조건을 모두 통과했다면 가능성 있는 숫자로 카운트
        if is_possible:
            possible_answer_count += 1
            
    # 5. 최종 개수 출력
    print(possible_answer_count)

if __name__ == '__main__':
    main()