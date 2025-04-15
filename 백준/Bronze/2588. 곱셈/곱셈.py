def bitwise_multiply_verbose(a, b):
    b_str = str(b)  # 문자열로 처리
    steps = []

    for i in reversed(b_str):  # 일의 자리부터 처리
        digit = int(i)
        partial = a * digit
        steps.append(partial)

    total = a * b
    return steps + [total]

# 입력
a = int(input())
b = int(input())

# 출력
for x in bitwise_multiply_verbose(a, b):
    print(x)