def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    min_value = min(arr)
    
    # 가장 작은 수를 제거한 배열 반환
    return [num for num in arr if num != min_value]