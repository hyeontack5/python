# 문자열처리함수

python = "Python is Amazing"
# 모두 소문자로 출력되게 한다.
print(python.lower())
# 모두 대문자로 출력되게 한다.
print(python.upper())

# python 변수의 0번째 인덱스가 대문자인지 여부를 boolean으로 알려준다.
print(python[0].isupper())

# python 변수의 길이를 알려준다.
print(len(python))

# python 변수의 Python 부분을 Java로 변경해준다.
print(python.replace("Python", "Java"))
print(python)

# python 변수에서 n이라는 문자가 몇 번째 있는지 알려준다.
index = python.index("n")
print(index)
# python 변수에서 n이라는 문자를 index
index = python.index("n", index + 1)
print(index)

'''
python.find 와 python.index의 차이를 기억할 것!
'''
print(python.find("n"))
# 요청한 값이 없으면 error를 출력하고 프로그램을 종료한다.
# print(python.index("Java"))
# 요청한 값이 없으면 -1을 출력하고 뒤이어 프로그램을 실행한다.
print(python.find("Java")) 
print("hi")

# python이라는 변수에서 n이 몇 번 있는지 알려준다.
print(python.count("n"))