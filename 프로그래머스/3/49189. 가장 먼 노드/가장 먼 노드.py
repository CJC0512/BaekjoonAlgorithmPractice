from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)
    
    distances = [-1] * (n+1)  
    distances[1] = 0  
    queue = deque([1])  
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    max_distance = max(distances)
    
    return distances.count(max_distance)