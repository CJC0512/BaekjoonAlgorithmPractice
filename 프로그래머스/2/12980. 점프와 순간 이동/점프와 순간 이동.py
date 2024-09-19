def solution(n):
    ans = 0
    
    # N이 0이 될 때까지 반복
    while n > 0:
        # N의 이진수 표현에서 가장 오른쪽 비트가 1이면 점프
        ans += n & 1
        # N을 2로 나눔 (순간이동을 한 것으로 처리)
        n //= 2
    
    return ans