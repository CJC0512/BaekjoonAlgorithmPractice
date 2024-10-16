def solution(n, lost, reserve):
    stu_list = []
    for i in range(1, n + 1):
        if i not in lost:
            stu_list.append(i)
                
    sorted_reserve = sorted(reserve)
            
    remain = []
    for rsv in sorted_reserve:
        print(rsv)
        if rsv in lost:
            stu_list.append(rsv)
        else:
            remain.append(rsv)
        
    for rem in remain:
        if (rem - 1) > 0 and ((rem - 1) not in stu_list):
            stu_list.append(rem - 1)
        elif (rem + 1) <= n and ((rem + 1) not in stu_list):
            stu_list.append(rem + 1)

    return len(stu_list)