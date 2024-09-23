def solution(brown, yellow):
    total = brown + yellow  # 전체 카펫의 격자 수

    # 가능한 height를 탐색 (최소 3부터 시작)
    for height in range(3, total // 3 + 1):
        if total % height == 0:  # 전체 격자 수가 height로 나누어 떨어져야 함
            width = total // height
            # 노란색 격자가 조건을 만족하는지 확인
            if (width - 2) * (height - 2) == yellow:
                return [width, height]

