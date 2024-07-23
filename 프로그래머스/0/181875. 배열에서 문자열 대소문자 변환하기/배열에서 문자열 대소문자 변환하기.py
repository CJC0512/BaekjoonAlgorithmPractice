def solution(strArr):
    answer = []
    for i, s in enumerate(strArr):
        if i % 2 == 0:
            answer.append(s.lower())
        else:
            answer.append(s.upper())
    return answer
