def solution(n):
    answer = []
    i = 0
    while(n > 0):
        answer.append(n % 10)
        n = n // 10
    return answer