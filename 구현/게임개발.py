"""
N*M의 직사각형으로 각각의 칸은 육지 또는 바다이다. 
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다. 
2. 캐릭터의 왼쪽 방향에 가보지 않은칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감. 
3. 만약 네 방향 모두 가본 칸이거나 바다로 되어있는 칸인 경우, 바라보는 방향을 유지한채로 한칸 뒤로 가고 1단계로 돌아간다. 
뒤쪽방향이 바다인 칸이라 뒤로 갈 수 없는 경우에 움직임을 멈춘다. 
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
