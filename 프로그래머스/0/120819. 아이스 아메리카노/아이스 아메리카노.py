def solution(money):
    price_of_americano = 5500
    count = money // price_of_americano  # 최대 잔 수
    remainder = money % price_of_americano  # 남은 돈
    return [count, remainder]
