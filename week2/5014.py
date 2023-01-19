from collections import deque

f, s, g, u, d = map(int, input().split())

queue = deque()
queue.append(s)

visited = [-1] * (f + 1)
visited[s] = 0

noans = True
while queue:
    cur = queue.popleft()

    if cur == g: # 도착
        print(visited[cur])
        noans = False
        break
    for next in (cur + u, cur - d): # 다음 층
        if 0 < next <= f and visited[next] == -1:
            queue.append(next)
            visited[next] = visited[cur] + 1

if(noans):
  print("use the stairs")
