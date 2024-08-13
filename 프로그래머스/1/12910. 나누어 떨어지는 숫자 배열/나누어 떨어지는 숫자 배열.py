def solution(arr, divisor):
    # divisor로 나누어 떨어지는 값을 리스트에 저장
    answer = [num for num in arr if num % divisor == 0]
    
    if not answer:
        return [-1]
    
    return sorted(answer)
