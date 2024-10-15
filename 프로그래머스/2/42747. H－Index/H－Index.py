def solution(citations):
    answer = 0
    sorted_sitations = sorted(citations, reverse=True)
    nlist = sorted([i for i in range(0, max(citations)+1)], reverse=True)
    for count in nlist:
        tmp = 0
        for sit in sorted_sitations:
            if sit >= count:
                tmp += 1
                if tmp >= count:
                    return count
    return answer