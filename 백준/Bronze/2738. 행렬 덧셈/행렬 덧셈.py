N, M = map(int, input().split())
a = []
b = []
for i in range(N):
    a.append(list(map(int, input().split())))
for i in range(N):
    b.append(list(map(int, input().split())))
for i in range(N):
    c = []
    for j in range(M):
        c.append(a[i][j]+b[i][j])
    print(*c)