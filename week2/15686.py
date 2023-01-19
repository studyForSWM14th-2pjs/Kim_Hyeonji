import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = []
for _ in range(n):
  city.append(list(map(int, input().split())))

anser = 99999
home = []
c_home = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            c_home.append([i, j])

for c in combinations(c_home, m):
    temp = 0
    for h in home: 
        dist = 99999
        for c_1 in c:
            dist = min(dist, abs(h[0] - c_1[0]) + abs(h[1] - c_1[1]))
        temp += dist
    anser = min(anser, temp)

print(anser)

# 런타임에러...