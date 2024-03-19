word = input().upper()  # 입력된 단어를 모두 대문자로 변환합니다.
count = [0] * 26  # 알파벳의 등장 횟수를 저장하기 위한 리스트입니다.

for char in word:
    if char.isalpha():  # 알파벳인 경우에만 처리합니다.
        count[ord(char) - 65] += 1  # 알파벳의 등장 횟수를 증가시킵니다.

max_count = max(count)  # 가장 많이 등장한 알파벳의 횟수를 구합니다.
max_index = count.index(max_count)  # 가장 많이 등장한 알파벳의 인덱스를 구합니다.

# 가장 많이 등장한 알파벳의 횟수가 1보다 크면 즉 같은 알파벳이 2개 이상이면
if count.count(max_count) > 1:
    print("?")
else:
    # 가장 많이 등장한 알파벳의 인덱스를 대문자로 변환하여 출력합니다.
    print(chr(max_index + 65))