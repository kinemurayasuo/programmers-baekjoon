a = []
maxValue = 0

for i in range(9):
    list_a = list(map(int, input().split()))
    maxValue_a = max(list_a)
    
    if maxValue <= maxValue_a:
        maxValue = maxValue_a
        max_row = i + 1
        max_col = list_a.index(maxValue_a) + 1

print(maxValue)
print(max_row, max_col)
        