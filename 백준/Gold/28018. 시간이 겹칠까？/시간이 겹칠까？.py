n = int(input())

time = [0]*1000002

for i in range(n):
    s, e = map(int, input().split())
    time[s] += 1
    time[e+1] -= 1
    
for i in range(1, len(time)):
    time[i] += time[i - 1]

count_hour = int(input())

hour_list = list(map(int, input().split()))

for i in range(count_hour):
    print(time[hour_list[i]])
    