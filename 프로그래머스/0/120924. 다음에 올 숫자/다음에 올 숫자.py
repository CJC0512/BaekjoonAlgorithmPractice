def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        # 등차수열인 경우
        d = common[1] - common[0]
        return common[-1] + d
    else:
        # 등비수열인 경우
        r = common[1] / common[0]
        return common[-1] * r