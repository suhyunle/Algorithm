""""
체스판이 8x8 크기야. (a1 ~ h8)
나이트가 현재 위치에서 이동할 수 있는 경우의 수를 구하는 문제다.
나이트의 이동 방식은 아래처럼 L자 형태로 총 8가지 방향이 있다.

input_data= input()
rpw= int (input_data[1])
column = int (ord(input_data[0])) - int(ord('a'))+1

steps =[(-2,-1),(-1,-3)]

"""
# 입력 예시: "a1"
input_pos = input()

# 열(문자), 행(숫자) 추출
col = ord(input_pos[0]) - ord('a') + 1  # a=1, b=2, ...
row = int(input_pos[1])

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 이동 가능한 경우의 수 체크
count = 0
for dx, dy in steps:
    next_row = row + dx
    next_col = col + dy
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        count += 1

print(count)

