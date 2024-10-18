from collections import deque

def solution(maps):
    width = len(maps[0])
    height = len(maps)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(x, y):
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if nx < 0 or ny < 0 or nx >= height or ny >= width:
                    continue
                
                if maps[nx][ny] == 0:
                    continue
                
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        
        return maps[height - 1][width - 1]
    
    answer = bfs(0, 0)
    
    return answer if answer > 1 else -1