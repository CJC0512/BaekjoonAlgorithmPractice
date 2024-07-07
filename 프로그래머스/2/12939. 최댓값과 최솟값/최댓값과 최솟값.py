def solution(s):
    numbers = list(map(int, s.split()))
    
    min_value = min(numbers)
    max_value = max(numbers)
    
    answer = f"{min_value} {max_value}"
    return answer