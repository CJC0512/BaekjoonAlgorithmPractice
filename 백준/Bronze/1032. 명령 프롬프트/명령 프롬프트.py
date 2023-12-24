N = int(input())
file_names = [input().strip() for _ in range(N)]

pattern = list(file_names[0])
name_length = len(pattern)

for i in range(1, N):
    for j in range(name_length):
         if file_names[i][j] != pattern[j] and pattern[j] != '?':
            pattern[j] = '?'

result = "".join(pattern)
print(result)
