N, K = map(int, input().split())  # 동전의 종류 수 N, 목표 가치 K 입력
coins = []  # 동전의 가치를 저장할 리스트

# 동전의 가치를 입력받아 리스트에 저장
for _ in range(N):
    coin = int(input())
    coins.append(coin)

count = 0  # 필요한 동전의 개수를 카운트하는 변수
# 가장 가치가 큰 동전부터 사용하여 목표 가치 K를 만들어 나간다.
for i in range(N - 1, -1, -1):
    if K == 0:  # 목표 가치 K가 0이 되면 반복문을 종료한다.
        break
    # 현재 가치의 동전을 몇 개 사용할 수 있는지 계산하고 K에서 그만큼 차감한다.
    count += K // coins[i]
    K %= coins[i]

print(count)  # 필요한 동전의 개수를 출력한다.