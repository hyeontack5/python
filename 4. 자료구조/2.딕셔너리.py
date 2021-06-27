# dictionary : 딕셔너리

# key:value 형식
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# error를 출력하고 프로그램을 종료한다.
# print(cabinet[5])
# None을 출력하고 뒤이어 프로그램을 실행한다.
print(cabinet.get(5))
# None이라는 문자 말고 다른 문자를 default로 출력하게 하려면
print(cabinet.get(5, "사용 가능"))
print("hi")

# 사전에 키 값이 있는지 확인하는 방법
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 사전에서 키 값 등록하는 방법
print(cabinet)
# 키 값이 사전에 이미 있으면 값을 update 한다.
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 사전에서 키 값 삭제하는 방법
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 사전 모두 지우는 법
cabinet.clear()
print(cabinet)