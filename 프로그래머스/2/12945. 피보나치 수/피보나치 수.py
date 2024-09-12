def solution(n):
    # 피보나치 수를 저장할 리스트 생성 (0번째와 1번째는 미리 설정)
    fibo = [0] * (n + 1)
    fibo[1] = 1
    
    # 피보나치 수 계산 (동적 프로그래밍 사용)
    for i in range(2, n + 1):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1234567
    
    # n번째 피보나치 수 리턴
    return fibo[n]
