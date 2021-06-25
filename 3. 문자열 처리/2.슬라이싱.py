# 슬라이싱

hyeontack5 = "951234-1234567"

# 인덱스는 0부터 시작한다.
print("성별 : " + hyeontack5[7])
print("연 : " + hyeontack5[0:2]) # 인덱스 0 ~ 2 직전까지 (0, 1)
print("월 : " + hyeontack5[2:4])
print("월 : " + hyeontack5[4:6])

print("생년월일 : " + hyeontack5[0:6])
print("생년월일 : " + hyeontack5[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + hyeontack5[7:14])
print("뒤 7자리 : " + hyeontack5[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에 부터) : " + hyeontack5[-7:]) # 맨 뒤에서 7번째 부터 끝까지
# 뒤에서 부터 가는 인덱스는 -1 부터 시작한다.
