def solution(sizes):
    # 명함을 회전시켜 가로는 항상 큰 값, 세로는 작은 값이 되도록 한다.
    rotated_sizes = [(max(w, h), min(w, h)) for w, h in sizes]
    
    # 가로 길이 중 최대값, 세로 길이 중 최대값을 찾는다.
    max_width = max(size[0] for size in rotated_sizes)
    max_height = max(size[1] for size in rotated_sizes)
    
    # 두 최대값을 곱한 값이 최소 직사각형의 크기
    return max_width * max_height
