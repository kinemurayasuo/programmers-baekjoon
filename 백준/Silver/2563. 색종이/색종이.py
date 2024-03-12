n = int(input()) # 랜덤 색종이 생성
ary = [[0]*100 for _ in range(100)] # 100 * 100 도화지 2차원 배열 생성

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(y, y+10):
        index_y = i # x 좌표 점 찍기
        for j in range(x, x+10):
            index_x = j
            if ary[index_y][index_x] == 0:
                ary[index_y][index_x] = 1
            else:
                pass
            
result = 0
for i in range(100):
    result += sum(ary[i])
print(result)
            
        
        