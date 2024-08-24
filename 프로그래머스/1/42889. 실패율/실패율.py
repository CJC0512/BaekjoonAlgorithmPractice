def solution(N, stages):
    # 각 스테이지의 실패율을 계산하기 위한 리스트
    failure_rates = []
    # 게임을 이용하는 총 사용자 수
    total_users = len(stages)
    
    for i in range(1, N + 1):
        # 해당 스테이지에 도달한 사용자 수
        reached = stages.count(i)
        
        # 실패율 계산: 스테이지에 도달했으나 클리어하지 못한 플레이어 수 / 도달한 플레이어 수
        if total_users > 0:
            failure_rate = reached / total_users
        else:
            failure_rate = 0
        
        # 해당 스테이지 번호와 실패율을 튜플로 저장
        failure_rates.append((i, failure_rate))
        
        # 총 사용자 수에서 해당 스테이지에 도달한 사용자 수를 빼줌
        total_users -= reached
    
    # 실패율을 기준으로 내림차순 정렬하되, 실패율이 동일할 경우 스테이지 번호 순으로 정렬
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    # 정렬된 스테이지 번호만 반환
    answer = [stage[0] for stage in failure_rates]
    
    return answer
