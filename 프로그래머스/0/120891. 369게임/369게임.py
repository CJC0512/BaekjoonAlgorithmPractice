

def solution(order):
    answer = 0
    while order:
        digit = order % 10
        if digit in [3, 6, 9]:
            answer += 1
        order //= 10
    return answer