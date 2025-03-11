"""

여행가 A N*N 직사각형 앞에 서있음. 
L: 왼쪽으로 한 칸 이동 
R: 오른쪽으로 한칸 이동
U: 위로 한칸 이동
D: 아래로 한칸 이동. 


"""
n= int(input())
x,y=1,1
plans = input().split()

#L,R,U,D에 따른 이동방향. 
move_types =['L','R','U','D']


#이동 계획을 하나씩 확인
for plan in plans: 
  if plan == move_types[i]:
    nx=x+dx[i]
    ny=y+dy[i]
    
  #이동후 좌표 구하기 


#공간을 벗어나는 경우 무시
if nx<1 or my <1 or nx>n or ny>n:
  continue
  #이동수행
  x,y =nx,ny


print(x,y)
