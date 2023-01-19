f = [1,2]
for i in range(2, 43):
    f.append(f[i-2]+f[i-1]) 
N = int(input())

for j in range(N):
    n = int(input())
    result=[]
    while(n):
        for i in range(43):
            if(f[i]<=n):
                m = f[i]
        n -= m
        result.append(m)
        result.sort()
    for b in range(len(result)):
        print(result[b], end=' ')