def solution(k, tangerine):
    size_count = {}
    
    # 각 귤 크기별로 개수 세기
    for size in tangerine:
        if size in size_count:
            size_count[size] += 1
        else:
            size_count[size] = 1
    
    # 빈도(개수)별로 내림차순 정렬
    sorted_sizes = sorted(size_count.values(), reverse=True)
    
    # 가장 적은 종류로 k개 이상을 선택하기
    count = 0
    for size in sorted_sizes:
        k -= size
        count += 1
        if k <= 0:
            break
    
    return count
