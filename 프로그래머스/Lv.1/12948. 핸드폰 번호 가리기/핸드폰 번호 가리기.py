def solution(phone_number):
    length = len(phone_number)
    answer = (''.zfill(length-4)).replace("0","*") + phone_number[-4:]
    print(answer)
    return answer