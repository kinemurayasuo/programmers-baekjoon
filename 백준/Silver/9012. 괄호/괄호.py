def is_vps(s):
    stack = []
    bracket_pairs = {')': '('}  # 닫는 괄호와 대응하는 여는 괄호 매핑

    for char in s:
        if char in bracket_pairs.values():  # 여는 괄호라면 스택에 추가
            stack.append(char)
        elif char in bracket_pairs.keys():  # 닫는 괄호라면
            if not stack or bracket_pairs[char] != stack.pop():  # 스택이 비어있거나 대응하는 여는 괄호가 아니라면
                return "NO"
    
    if not stack:  # 스택이 비어있다면 올바른 괄호 문자열
        return "YES"
    else:
        return "NO"

# 입력 받기
T = int(input())  # 테스트 케이스의 수
for _ in range(T):
    parentheses = input()  # 괄호 문자열
    print(is_vps(parentheses))