def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        count = 0
        
        # 대칭에 의한 범위 설정
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                count += 1
                if i != num // i:  # i와 num // i가 다르면 두 개의 약수를 추가
                    count += 1
        
        # 약수의 개수가 짝수면 더하고, 홀수면 뺀다
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
            
    return answer
