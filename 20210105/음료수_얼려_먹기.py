# N, M 입력 받기
n, m = map(int, input().split())

graph = list()

# 2차원 그래프 입력 받기
for i in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x, y):
    # 범위에 벗어나는 경우 즉시 중지
    if x <= -1 or x>=n or y<=-1 or y>=m:
        return False
    
    # 현재 노드에 방문하지 않았다면 진행
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상 하 좌 우 노드 방문
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
        
    return False
    

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
            
print(result)
