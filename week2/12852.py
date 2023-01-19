import sys
from collections import deque

input = sys.stdin.readline

num = int(input())
queue = deque()
queue.append([num])
answer = []

while queue:
  nums = queue.popleft()
  n = nums[0]
  if n == 1:
    answer = nums
    break
  
  if n % 3 == 0:
    queue.append([n//3]+nums)
  if n % 2 == 0:
    queue.append([n//2]+nums)
  
  queue.append([n-1]+nums)

print(len(answer) - 1)
print(*answer[::-1])

# 시간초과