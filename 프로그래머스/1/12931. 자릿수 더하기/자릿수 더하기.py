def solution(n):
    # 각 자릿수를 더한 값을 계산
    answer = sum(int(digit) for digit in str(n))
    return answer
