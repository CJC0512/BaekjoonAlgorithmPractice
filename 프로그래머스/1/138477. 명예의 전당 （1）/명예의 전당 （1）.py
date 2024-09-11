def solution(k, score):
    hall_of_fame = []
    result = []
    
    for s in score:
        hall_of_fame.append(s)
        hall_of_fame.sort(reverse=True)  # 내림차순으로 정렬
        if len(hall_of_fame) > k:
            hall_of_fame.pop()  # 최하위 점수를 제거
        
        result.append(hall_of_fame[-1])  # 현재 명예의 전당의 최하위 점수 기록
    
    return result
