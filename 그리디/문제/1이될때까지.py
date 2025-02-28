"""
어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 

1. N에서 1을 뺀다. 
2. N을 K로 나눈다. 

예를들어 n이 k가 4라고 가정하자. 이때 1번의 과정을 수행하면 N은 16이 된다. 이후에 2번의 과정을 두번 수행하면
N은 1이된다. 결과적으로 이 경우 전체과정을 실행한 횟수는 3이된다. 
N을 1로 만드는 최소 횟수이다. 

N과 K 가 주어질때 N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하는 프로그램을 작성하시오. 
"""
#1.
n,k = map(int, input().split())
result =0 

while n>= k :
  #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
  while n%k !=0:
    n-=1
    result +=1

#마지막으로 남은 수에 대하여 1씩 빼기

while n>1:
  n-=1
  result +=1

print(result)

#2. 

N, K를 공백으로 하여 입력받기. 
n,k =map(int,input().split())
result =0

while True:
  #(N==K로 나누어 떨어지는 수 )가 될때까지 1씩 빼기 .
  target = (n//k)*k
  
"""
n // k : n을 k로 나눈 몫을 구함 (소수점 버림)
* k : 그 몫을 다시 k로 곱해서 k의 배수를 만듦
즉, target은 n보다 작거나 같은 가장 가까운 k의 배수가 됨.
"""

  result += (n-target)
  n= target

# N이 K보다 작을때(더이상 나눌 수 없을 때 반복문 탈출)
if n<k:
  break

#k로 나누기
result += 1
n//=k

#마지막으로 남은수에 대하여 1씩 빼기 

result+=(n-1)
print(result)
