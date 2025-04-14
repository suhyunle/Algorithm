#미로탈출 
"""
N × M 크기의 미로에 갇혀 있다.
미로는 여러 개의 칸(격자)으로 구성되어 있고,
각 칸은 1(길) 또는 0(벽)로 표시되어 있다.

당신은 (1, 1)에서 시작해서 (N, M) 위치까지 이동해야 함.
이동할 때는 상, 하, 좌, 우로 한 칸씩 이동 가능함.

구현 방법: BFS 너비우선탐색
"""

n,m= map(int,input().split())
road =[list(map(int, input())) for i in range(n)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def escape(x,y):
    queue = [(x,y)]
    
    while queue:
        x,y=queue[0]   # 큐의 첫 번째 원소
        queue=queue[1:] # pop(0)과 같은 효과

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>= n or ny>= m:
                continue

            
            if road[nx][ny]== 0:
                continue

            # 처음 방문하는 길이라면 거리기록
            if road[nx][ny] == 1:
                road[nx][ny] = road[x][y] +1
                queue.append((nx, ny))

    return road[n-1][m-1]

print(escape(0, 0))
