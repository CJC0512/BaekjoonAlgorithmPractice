N = int(input())

length = 0
digit = 1
start = 1

while start <= N:
    end = min(N, start * 10 - 1)
    length += (end - start + 1) * digit
    digit += 1
    start *= 10

print(length)