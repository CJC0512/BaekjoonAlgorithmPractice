from itertools import combinations

def solution(number):
    answer = 0
    # 3명의 학생을 선택하는 모든 조합을 확인
    for comb in combinations(number, 3):
        if sum(comb) == 0:  # 3명의 합이 0이면 삼총사로 인정
            answer += 1
    return answer
