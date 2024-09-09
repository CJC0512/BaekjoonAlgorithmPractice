def solution(a, b, n):
    total_cola = 0
    
    while n >= a:
        new_cola = (n // a) * b  # 콜라를 받을 수 있는 개수
        total_cola += new_cola  # 총 받은 콜라 개수에 추가
        n = (n % a) + new_cola  # 남은 병 개수에 새로 받은 콜라의 병 개수를 더한다
    
    return total_cola