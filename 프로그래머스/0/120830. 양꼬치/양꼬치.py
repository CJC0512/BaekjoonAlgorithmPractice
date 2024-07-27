def solution(n, k):
    kebab_cost = n * 12000
    free_drinks = n // 10
    paid_drinks = k - free_drinks
    drink_cost = paid_drinks * 2000
    total_cost = kebab_cost + drink_cost
    return total_cost
