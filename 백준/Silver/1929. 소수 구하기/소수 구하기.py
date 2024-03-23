import math

def sieve_of_eratosthenes(M, N):
    prime = [True] * (N+1)  # 0부터 N까지의 숫자가 소수인지 여부를 저장하는 리스트를 생성합니다.
    prime[0] = prime[1] = False  # 0과 1은 소수가 아니므로 False로 설정합니다.

    # 에라토스테네스의 체 알고리즘을 이용하여 소수를 찾습니다.
    for i in range(2, int(math.sqrt(N))+1):
        if prime[i]:
            # i의 배수들을 소수가 아닌 것으로 표시합니다.
            for j in range(i*i, N+1, i):
                prime[j] = False

    # 소수를 출력합니다.
    for num in range(M, N+1):
        if prime[num]:
            print(num)

# 입력값을 받습니다.
M, N = map(int, input().split())

# 소수 찾기 함수를 호출하여 출력합니다.
sieve_of_eratosthenes(M, N)