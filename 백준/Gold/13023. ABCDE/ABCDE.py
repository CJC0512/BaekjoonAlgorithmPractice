def solution(n, m):
    # 사람 수 만큼 관계 리스트 만들기
    mate = [[] for _ in range(n)]
    
    # 관계 적용
    for i in range(m):
        n1, n2 = map(int, input().split())
        mate[n1].append(n2)
        mate[n2].append(n1)
        
    visited = [0] * n
    
    def dfs(v, depth):
        # A-B-C-D-E 5명이므로 4
        if depth == 4:
            return 1
        
        visited[v] = 1
        
        for i in mate[v]:
            if not visited[i]:
                if dfs(i, depth + 1):
                    return 1
                
        visited[v] = 0
    
    for i in range(n):
        if dfs(i, 0):
            return 1
        
    return 0
    
    
def main():
    n, m = map(int, input().split())
    print(solution(n, m))
    
if __name__ == "__main__":
    main()