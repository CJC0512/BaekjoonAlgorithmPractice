def solution(k, m, score):
    score.sort(reverse=True)
    total_profit = 0
    
    # m개씩 그룹으로 나누어 최저 점수를 기준으로 가격 계산
    for i in range(0, len(score) - m + 1, m):
        # 한 상자의 최저 점수는 해당 그룹에서 마지막 사과의 점수
        box_score = score[i + m - 1]
        total_profit += box_score * m
    
    return total_profit
