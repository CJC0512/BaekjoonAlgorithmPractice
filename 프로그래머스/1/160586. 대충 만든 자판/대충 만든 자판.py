def solution(keymap, targets):
    press_count = {}

    for key in keymap:
        for idx, char in enumerate(key):
            if char not in press_count:
                press_count[char] = idx + 1  # 인덱스는 0부터 시작하므로 +1
            else:
                press_count[char] = min(press_count[char], idx + 1)

    answer = []

    for target in targets:
        total_presses = 0
        for char in target:
            if char in press_count:
                total_presses += press_count[char]
            else:
                total_presses = -1
                break

        answer.append(total_presses)

    return answer
