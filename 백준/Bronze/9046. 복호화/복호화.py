for _ in range(int(input())):
    text = input().replace(" ", "")
    counter = {}
    for char in text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    max_count = max(counter.values())
    most_common = [char for char, count in counter.items() if count == max_count]
    if len(most_common) == 1:
        print(most_common[0])
    else:
        print("?")