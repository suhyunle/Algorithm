# Algorithm
알고리즘 개념 및 문제풀이
📌 1. 입출력 최적화
대량의 데이터를 입력받을 때 sys.stdin.readline()을 사용하면 훨씬 빠름!

python
복사
편집
import sys
input = sys.stdin.readline  # 이렇게 설정하면 input() 대신 사용 가능

n = int(input())  # 숫자 입력받기
arr = list(map(int, input().split()))  # 여러 개 숫자 입력받기
🚀 Tip: rstrip()을 사용하면 개행 문자 제거 가능

python

s = input().rstrip()
📌 2. 리스트 & 문자열 조작
📍 리스트 정렬
python

arr = [3, 1, 4, 1, 5]
arr.sort()  # 오름차순 정렬
print(arr)  # [1, 1, 3, 4, 5]

arr.sort(reverse=True)  # 내림차순 정렬
print(arr)  # [5, 4, 3, 1, 1]
🚀 Tip: sorted(arr, key=lambda x: (우선순위1, 우선순위2))


people = [(25, 'Alice'), (30, 'Bob'), (22, 'Charlie')]
people.sort(key=lambda x: (x[0], x[1]))  # 나이 오름차순, 같은 나이면 이름순 정렬

📍 문자열 조작
s = "hello world"
print(s.split())  # ['hello', 'world']
print("-".join(["A", "B", "C"]))  # "A-B-C"
📌 3. 딕셔너리 & 집합
📍 딕셔너리 (Counter 활용)
python
복사
편집
from collections import Counter

arr = ["apple", "banana", "apple", "orange", "banana", "banana"]
counter = Counter(arr)
print(counter)  # {'banana': 3, 'apple': 2, 'orange': 1}
print(counter.most_common(1))  # [('banana', 3)]
📍 집합 (중복 제거)
python
복사
편집
s = set([1, 2, 3, 3, 2])
s.add(4)
print(s)  # {1, 2, 3, 4}
📌 4. 스택, 큐, 우선순위 큐
📍 스택 (LIFO)
python
복사
편집
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())  # 2 (마지막 값 꺼내기)
📍 큐 (FIFO)
python
복사
편집
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
print(queue.popleft())  # 1 (맨 앞 값 꺼내기)
📍 우선순위 큐 (최소 힙)
python
복사
편집
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
print(heapq.heappop(heap))  # 1 (가장 작은 값 꺼내기)
📌 5. 완전탐색 & 백트래킹
📍 모든 순열 (permutations)
python
복사
편집
from itertools import permutations

arr = [1, 2, 3]
print(list(permutations(arr)))  # [(1,2,3), (1,3,2), (2,1,3), ...]
📍 모든 조합 (combinations)
python
복사
편집
from itertools import combinations

arr = [1, 2, 3, 4]
print(list(combinations(arr, 2)))  # [(1,2), (1,3), (1,4), ...]
📌 6. 이진 탐색 (bisect 라이브러리)
📍 특정 값이 들어갈 위치 찾기
python
복사
편집
import bisect

arr = [1, 3, 5, 7]
idx = bisect.bisect_left(arr, 4)  # 4가 들어갈 왼쪽 인덱스
print(idx)  # 2
