def parenthesis(x):
    stack = []
    for i in x:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return "NO"
            else:
                stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"
    
a = int(input())
for _ in range(a):
    x = input()
    print(parenthesis(x))

    