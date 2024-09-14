def solution(s):
    # 각 단어별로 처리하기 위해 문자열을 공백으로 나눔
    words = s.split(' ')
    result = []

    for word in words:
        new_word = ''
        for i, char in enumerate(word):
            # 짝수 번째는 대문자, 홀수 번째는 소문자
            if i % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        result.append(new_word)

    # 공백을 기준으로 단어들을 다시 결합
    return ' '.join(result)
