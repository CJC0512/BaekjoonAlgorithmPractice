def solution(X, Y):
    count_X = [0] * 10
    count_Y = [0] * 10
    
    for digit in X:
        count_X[int(digit)] += 1
    
    for digit in Y:
        count_Y[int(digit)] += 1
    
    result = []
    
    # 0부터 9까지 숫자 중 공통된 것들을 찾기
    for digit in range(9, -1, -1):  # 큰 숫자부터 내림차순으로 탐색
        count_common = min(count_X[digit], count_Y[digit])
        result.append(str(digit) * count_common)
    
    answer = ''.join(result)
    
    if answer == "":
        return "-1"
    if answer[0] == "0":
        return "0"
    
    return answer
