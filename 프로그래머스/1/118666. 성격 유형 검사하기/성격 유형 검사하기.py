def solution(survey, choices):
    score_map = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    
    # 점수 계산을 위한 choice 값별 점수
    choice_scores = [3, 2, 1, 0, 1, 2, 3]
    
    # survey와 choices를 순차적으로 처리
    for i in range(len(survey)):
        first, second = survey[i][0], survey[i][1]
        choice = choices[i]
        
        if choice < 4:
            score_map[first] += choice_scores[choice - 1]
        elif choice > 4:
            score_map[second] += choice_scores[choice - 1]
    
    # 각 지표에서 더 높은 점수를 받은 성격 유형을 선택
    answer = ''
    answer += 'R' if score_map['R'] >= score_map['T'] else 'T'
    answer += 'C' if score_map['C'] >= score_map['F'] else 'F'
    answer += 'J' if score_map['J'] >= score_map['M'] else 'M'
    answer += 'A' if score_map['A'] >= score_map['N'] else 'N'
    
    return answer
