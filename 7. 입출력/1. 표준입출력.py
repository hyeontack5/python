# 표준입출력

# print 함수는 기본적으로 sep=" " 인데 생략된 것이다.
# sep를 통해서 문자열에서 "," 부분을 어떻게 처리할 지 정해줄 수 있다.
print("Python", "Java")
print("Python", "Java", sep=" ")

print("Python", "Java", sep=",")
print("Python", "Java", sep=" vs ")

# print 함수는 기본적으로 end="\n" 인데 생략된 것이다.
# end를 통해서 print함수의 끝을 어떻게 처리할 지 정해줄 수 있다.
print("Python", "Java")
print("Python", "Java", end="\n")

print("Python", "Java", sep=",", end="?")
print("무엇이 더 재미있을까요?")

from os import sep
import sys
print("Python", "Java", file= sys.stdout)
print("Python", "Java", file= sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
# dictionary 는 .items()를 통해서 key:value 를 쌍으로 가져올 수 있다.
for subject, score in scores.items():
  # print(subject, score)
  # .ljust(n) : n 자리를 확보하고 왼쪽 정렬
  # .rjust(n) : n 자리를 확보하고 오른쪽 정렬
  print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번 포트
# 001, 002, 003, ...
for num in range(1, 21):
  # zfill(n) : n 자리를 확보하고 남는 자리는 zero 0 으로 채운다.
  print("대기번호 : " + str(num).zfill(3))

# 사용자 입력 input을 사용하게 되면 항상 string 타입으로 반환한다.
answer = input("아무 값이나 임력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")