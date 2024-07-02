def solution(intStrs, k, s, l):
    answer = []
    for string in intStrs:
        substring = string[s:s+l]
        num = int(substring)
        if num > k:
            answer.append(num)
    return answer
