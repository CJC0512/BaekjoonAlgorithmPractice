def solution(targets):
    # 구간을 끝나는 위치 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    
    answer = 0
    last_shot = -1  # 마지막으로 발사한 미사일의 위치를 기록
    
    for s, e in targets:
        # 현재 구간이 마지막 요격 미사일이 커버할 수 없는 경우
        if s >= last_shot:
            # 새로운 요격 미사일 발사
            last_shot = e
            answer += 1
    
    return answer
