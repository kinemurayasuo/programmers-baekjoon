# 입력 받기
n = int(input())  # 손님의 수
tips = []  # 손님이 주려고 생각하는 팁을 저장할 리스트
for _ in range(n):
    tip = int(input())
    tips.append(tip)

# 팁을 정렬
tips.sort(reverse=True)

# 강호가 받을 팁의 총합 계산
total_tip = 0
for i in range(n):
    tip = tips[i] - i  # 해당 손님이 받을 팁의 액수 계산
    if tip > 0:
        total_tip += tip
    else:
        break  # 팁이 음수가 되면 더 이상 계산하지 않고 종료

# 결과 출력
print(total_tip)