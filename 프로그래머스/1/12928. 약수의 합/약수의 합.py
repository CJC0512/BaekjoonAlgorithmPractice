def solution(n):
    answer = 0
    # 1부터 n까지 반복하면서 n의 약수인 경우에 더한다.
    for i in range(1, n + 1):
        if n % i == 0:  # i가 n의 약수인 경우
            answer += i
    return answer
