def solution(s):
    answer = []
    last_seen = {}  # 딕셔너리로 각 문자의 마지막 위치를 기록
    
    for i, char in enumerate(s):
        if char in last_seen:
            answer.append(i - last_seen[char])  # 현재 위치와 이전 위치의 차이를 계산
        else:
            answer.append(-1)  # 처음 등장하는 문자는 -1로 처리
        last_seen[char] = i  # 현재 문자의 마지막 위치를 갱신
    
    return answer