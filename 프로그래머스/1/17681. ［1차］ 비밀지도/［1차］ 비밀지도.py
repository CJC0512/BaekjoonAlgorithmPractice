def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        # 각 arr1[i]와 arr2[i]의 OR 연산 결과를 이진수로 변환
        combined = arr1[i] | arr2[i]
        
        # 이진수로 변환된 값을 n비트 길이의 문자열로 변환
        row = ""
        for j in range(n):
            # 각 비트가 1이면 '#', 0이면 ' '로 변환
            if combined & (1 << (n - j - 1)):
                row += "#"
            else:
                row += " "
        
        # 완성된 한 줄(row)을 결과 리스트에 추가
        answer.append(row)
    
    return answer
