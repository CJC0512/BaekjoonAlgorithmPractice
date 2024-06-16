def solution(n):
    sqrt_n = int(n ** 0.5)
    if sqrt_n * sqrt_n == n:
        return 1
    else:
        return 2