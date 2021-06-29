# 지역변수와 전역변수

# 전역 변수 gun
gun = 10

# 전역 변수를 이용한 함수 (권장 하는 방법은 아니다)
# 전역 변수를 가급적이면 안쓰고 함수의 return을 사용하는게 좋다
def checkpoint(soldiers): # 경계근무
  # 지역 변수 gun
  # gun = 20
  global gun  # global을 붙여서 전역 공간에 있는 gun 사용가능
  gun = gun - soldiers
  # gun -= solidiers 로 대체 할 수 있다.
  print("[함수 내] 남은 총 : {0}" .format(gun))

print("전체 총 : {0}" .format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}" .format(gun))

# 함수의 return을 사용하는 방법 (권장 하는 방법이다.)
def checkpoint_return(gun, soldiers):
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {0}" .format(gun))
  return gun

print("전체 총 : {0}" .format(gun))
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}" .format(gun))
