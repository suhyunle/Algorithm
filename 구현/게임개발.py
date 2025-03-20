"""
N*M의 직사각형으로 각각의 칸은 육지 또는 바다이다. 
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다. 
2. 캐릭터의 왼쪽 방향에 가보지 않은칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감. 
3. 만약 네 방향 모두 가본 칸이거나 바다로 되어있는 칸인 경우, 바라보는 방향을 유지한채로 한칸 뒤로 가고 1단계로 돌아간다. 
뒤쪽방향이 바다인 칸이라 뒤로 갈 수 없는 경우에 움직임을 멈춘다. 

구현은 말그래도 머릿속에 있는 알고리즘을 소스코드로 구현하는 과정이다. 

완전탐색과 시뮬레이션 유형 이 두가지로 구분할 수 있다.

 

완전탐색 : 모든 경우의 수를 주저 없이 다 계산하여 해결하는 유형

시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해서 문제를 해결하는 유형

 

문제를 접하면 차례대로 과정이 써있는 것을 보고 시뮬레이션으로 풀어야겠다란 생각을 해야한다.

기본 규칙 다시 쉽게!
1. 캐릭터의 움직임은?
반드시 왼쪽 방향부터 본다!
바라보는 방향 기준으로 **왼쪽 방향(반시계 방향)**부터 차례차례 갈 곳을 생각해.
만약 왼쪽에 가보지 않은 육지가 있다면 → 거기로 이동!
없으면 왼쪽으로 방향만 돌리고 다시 고민!
2. 네 방향 다 가봤거나 못 간다면?
뒤로 한 칸 후진해!
그런데 뒤가 바다라면?
→ 움직임 멈추고 게임 끝!
"""


n,m = map(int,input().split())
d=[[0] *m for _ in range(n)] #방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화 . 
x, y , direction = map(int, input().split())
d[x][y]=1 #현재좌표 방문 처리 
array=[]
for i in range(n):
  array.append(list(map(int,input().split())))
dx=[-1,0,1,0]  # 북, 동, 남 ,서 방향 정의
dy=[0,1,0,-1]

def turn_left(): #왼쪽으로 회전
  global direction
  direction = -1
  if direction ==-1:
    direction = 3

#시뮬레이션 시작.
count =1

turn_time=0
while True:
  turn_left() #왼쪽으로 회전
  nx= x+dx[direction]
  ny= y+dy[direction]

#회전 한 이후 정면에 가보지 않은 칸이 없거나 바다인 이유. 
else: 
  turn_time +=1
# 네 방향 모두 갈 수 없는 경우 . 
if turn_time ==4: 
  nx = x-dx[direction]
  ny= y- dy[direction]

#뒤로 갈 수 있다면 이동하기
if array[nx][ny]==0:
  x= nx
  y=ny
  #뒤가 바다로 막혀있는 경우
else:
  break
turn_time =0

print(count)




------

# 입력 받기
n, m = map(int, input().split())         # 맵 크기
x, y, direction = map(int, input().split()) # 캐릭터 좌표와 방향

# 맵 정보 입력 받기
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))

# 방문한 위치를 저장할 맵 생성 (처음 위치 방문 처리)
visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]  # 북, 동, 남, 서 (x 이동)
dy = [0, 1, 0, -1]  # 북, 동, 남, 서 (y 이동)

def turn_left():
    global direction
    direction = (direction - 1) % 4  # 반시계 방향 회전 (왼쪽 회전)

# 시작 위치 포함 방문한 칸 수
count = 1
# 회전한 횟수 (네 방향 모두 막히면 뒤로 가야 함)
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 왼쪽 방향에 가보지 않은 육지가 존재하면 이동
    if visited[nx][ny] == 0 and game_map[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0  # 이동했으니 회전 횟수 초기화
        continue
    else:
        turn_time += 1
    
    # 네 방향 모두 이동 불가하면
    if turn_time == 4:
        # 뒤로 이동하기
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤쪽이 육지라면 이동
        if game_map[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0  # 다시 초기화
        else:
            # 뒤가 바다라면 멈춤
            break

print(count)
---------------
n, m=map(int,input().split())
x,y,d=map(int, input().split())

#맵 정보 입력해 리스트에 저장
map_list=[]
for _ in range(n):
        row=list(map(int,input().split()))
        map_list.append(row)
map_list[x][y]=1

def rotation() :
    global d
    d-=1
    if d==-1 :
        d=3

dx=[-1,0,1,0]
dy=[0,1,0,-1]
#시뮬레이션 시작

cnt=1
rotation_cnt=0
while True : 
    rotation()
    nx=x+dx[d]
    ny=y+dy[d]

    #회전한 이후 정면에 가보지 않은 칸이 있는 경우
    if map_list[nx][ny]==0 :
        map_list[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        rotation_cnt=0
        continue
    else :
        rotation_cnt+=1
    
    #네 방향 모두 갈 곳이 없을 경우
    if rotation_cnt==4 :
        nx=x-dx[d]
        ny=y-dy[d]
        if map_list[nx][ny]==0 :
            x=nx
            y=ny
        #뒤가 바다일 경우 탈출
        else :
            break
        rotation_cnt=0

print(cnt)


