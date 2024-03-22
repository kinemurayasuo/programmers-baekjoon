def sieve_of_eratosthenes(M, N):
    prime_check = [True] * (N+1)
    prime_check[0] = prime_check[1] = False
    
    p = 2
    while p**2 <= N:
        if prime_check[p] == True:
            for i in range(p**2, N+1, p):
                prime_check[i] = False
        p += 1

    for num in range(M, N+1):
        if prime_check[num]:
            print(num)

# 입력 받기
M, N = map(int, input().split())

# 소수 찾기 및 출력
sieve_of_eratosthenes(M, N)