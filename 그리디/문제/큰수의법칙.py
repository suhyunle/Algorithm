"""
큰 수의 법칙은 일반적으로 통계 분야에서 다루어지는 내용이지만 동빈이는 본인만의 방식으로 다르게 사용하고 있다. 동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을때
주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 
단,  번호의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다. 


예를들어 순서대로 2.4.5.4.6으로 이루어진 배열이 있을때 M이 8 이고 k가 3이라고 가정하자. 
큰 수의 법칙에 따른 결과는 6+6+6+5+6+6+6+5 인 46이 된다. 

서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주된다. 



------------
그리디 알고리즘으로 큰수의 법칙 문제풀이. 

1. 주어진 배열을 정렬하여 가장 큰 수와 두번재로 큰 수를 쉽게 찾는다. 
2. 반복 규칙을 적용하여 더할 수를 결정한다. 
3. 최종합을 계산한다. 
# 입력 값 중에서 가장 큰 수와 두번째로 큰 수만 저장하면 됨. 연속으로 더할 수 있는 횟수는 최대 k번. 
가장 큰수를 K번 더하고  두번째로  큰;수를 한번 더하는 연산을 반복하면 됨. 

"""
#N,M,K를 공백으로 구분하여 입력받기 
n,m,k =map (int, input.split())

#N개의 수를 공백으로 구분하여 입력받기 
data = list (map(int,input().split)))

data.sort() #입력받은 수들 정렬하기 
first = data[n-1] #가장 큰수
second = data[n-2] #두번째로 큰 수

result =0 

while True: 
  for i in range(k): # 가장 큰수를 k번 더하기
    if m ==0: # m이 0이라면 반복문 탈출
      break
    result += second #두번째로 큰수 한번 더하기. 
    m-= 1 # 더할때마다 1씩빼기

print(result) # 최종 답안 출력


#2

#N,M,K를 공백으로 구분하여 입력받기 
n,m,k =map (int, input.split())

#N개의 수를 공백으로 구분하여 입력받기 
data = list (map(int,input().split)))

data.sort() #입력받은 수들 정렬하기 
first = data[n-1] #가장 큰수
second = data[n-2] #두번째로 큰 수

#가장 큰 수가 더해지는 횟수 계산
count = int (m/(k+1))*k
count+ = m % (k+1)

result =0
result += (count) * first #가장 큰 수 더하기 
result += (m-count) * second #두번째로 큰 수더하기

print(result)


#3 
# 입력 받기
n, m, k = map(int, input().split())  # n: 수의 개수, m: 더할 횟수, k: 가장 큰 수가 더해지는 횟수
arr = list(map(int, input().split()))  # 배열 받기

# 배열 정렬 (내림차순)
arr.sort(reverse=True)

# 가장 큰 수와 두 번째 큰 수
first = arr[0]
second = arr[1]

# 가장 큰 수가 k번, 두 번째 큰 수가 1번 더하는 규칙을 반복해서 합산
result = 0
while m > 0:
    # 가장 큰 수 k번 더하기
    for _ in range(k):
        if m == 0: break
        result += first
        m -= 1
    # 두 번째 큰 수 1번 더하기
    if m > 0:
        result += second
        m -= 1

print(result)


  



