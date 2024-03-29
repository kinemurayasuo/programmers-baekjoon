def josephus(N, K):
    # 1부터 N까지의 사람들을 리스트로 생성
    people = list(range(1, N + 1))
    # 결과를 저장할 리스트
    result = []
    # 제거할 사람의 인덱스
    idx = 0
    
    # 모든 사람이 제거될 때까지 반복
    while people:
        # 다음에 제거될 사람의 인덱스 계산
        idx = (idx + K - 1) % len(people)
        # 해당 인덱스에 있는 사람을 결과 리스트에 추가하고 리스트에서 제거
        result.append(people.pop(idx))
    
    return result

# 입력 받기
N, K = map(int, input().split())
# 요세푸스 순열 구하기
sequence = josephus(N, K)
# 결과 출력
print("<" + ", ".join(map(str, sequence)) + ">")