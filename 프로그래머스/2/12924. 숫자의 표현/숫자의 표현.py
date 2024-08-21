def solution(n):
    count = 0
    m = 1
    while m * (m + 1) // 2 <= n:
        if (n - m * (m + 1) // 2) % m == 0:
            count += 1
        m += 1
    return count
