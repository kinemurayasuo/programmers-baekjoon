import sys

# 초기 문자열 입력
left_stack = list(sys.stdin.readline().strip())
right_stack = []
# 커서의 위치를 나타내는 변수
cursor = len(left_stack)

# 명령어 개수 입력
n = int(sys.stdin.readline().strip())

# 명령어 처리
for _ in range(n):
    command = sys.stdin.readline().strip()

    if command == 'L':  # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.append(left_stack.pop())
            cursor -= 1
    elif command == 'D':  # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.pop())
            cursor += 1
    elif command == 'B':  # 왼쪽의 문자 삭제
        if left_stack:
            left_stack.pop()
            cursor -= 1
    elif command[0] == 'P':  # 문자 추가
        left_stack.append(command[2])
        cursor += 1

# 결과 출력
sys.stdout.write(''.join(left_stack + right_stack[::-1]))
