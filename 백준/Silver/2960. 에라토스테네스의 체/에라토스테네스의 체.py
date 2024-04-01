n , k = map(int, input().split())

def eratos(n, k):
  erato = [True] * (n+1)
  idx = 0
  
  for i in range(2, n+1):
    if erato[i]:
      for j in range(i, n+1, i):
        if erato[j]:
          erato[j] = False
          idx += 1
          if idx == k:
            return j

print(eratos(n, k))
