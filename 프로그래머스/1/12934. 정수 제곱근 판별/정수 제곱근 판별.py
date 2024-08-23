import math

def solution(n):
    sqrt_n = math.sqrt(n)  # n의 제곱근 계산
    if sqrt_n.is_integer():  # 제곱근이 정수인지 확인
        return int((sqrt_n + 1) ** 2)  # 정수라면, (sqrt_n + 1)의 제곱을 반환
    else:
        return -1  # 정수가 아니라면 -1 반환
