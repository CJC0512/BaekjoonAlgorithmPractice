N = int(input())
file_names = [input().strip() for _ in range(N)]

pattern = list(file_names[0])
name_length = len(file_names[0])

for i in range(N):
    for j in range(name_length):
         if file_names[i][j] != pattern[j]:
                if pattern[j] == '?':
                    continue
                else:
                    pattern[j] = '?'
                    
print("".join(pattern))