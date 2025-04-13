#미로탈출 
# 입력 받기
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 (리스트로 queue 구현)
def bfs(x, y):
    queue = [(x, y)]
    
    while queue:
        x, y = queue[0]   # 큐의 첫 번째 원소
        queue = queue[1:] # pop(0)과 같은 효과

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽이면 무시
            if graph[nx][ny] == 0:
                continue

            # 처음 방문하는 길이라면 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

# 결과 출력
print(bfs(0, 0))
