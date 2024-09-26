def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0  # 두 카드 뭉치의 인덱스

    for word in goal:
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1  # cards1에서 사용한 경우
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1  # cards2에서 사용한 경우
        else:
            return "No"  # 둘 다 맞지 않으면 "No" 반환

    return "Yes"  # 모든 단어를 사용하면 "Yes" 반환
