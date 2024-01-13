def solution(nums):
    max_count = len(nums) // 2
    unique_count = len(set(nums))
    
    answer = min(max_count, unique_count)
    
    return answer