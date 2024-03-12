x,y = map(int, input().split())

arr = list(range(x+1)) #배열인덱스 처음부터 +1씩 추가돼서 나옴

for _ in range(y): # for문 안에서 횟수 생성
    i,j = map(int, input().split())
    arr[i], arr[j] = arr[j], arr[i]

print(*arr[1:])
    