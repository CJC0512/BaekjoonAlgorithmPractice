def solution(diffs, times, limit):
    def can_solve_with_level(level):
        total_time = 0
        prev_time = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            
            if diff <= level:
                total_time += time_cur
            else:
                mistakes = diff - level
                total_time += (time_cur + prev_time) * mistakes + time_cur
            
            if total_time > limit:
                return False
            
            prev_time = time_cur
        
        return total_time <= limit

    # 이분 탐색 범위 설정 (1 ~ 100,000)
    low, high = 1, 100000
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if can_solve_with_level(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
