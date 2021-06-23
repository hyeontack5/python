# 변수

name = "오현택"
age = 28
hobby = "농구"
is_adult = age >= 19

print("안녕하세요 저의 이름은" + name + "입니다.")
print("나이는" + str(age) + "살이고 취미는 " + hobby + "입니다.")
# "," 를 사용하게 되면 자동으로 "," 뒤에 white space가 생깁니다.
print("나이는", str(age), "살이고 취미는", hobby, "입니다.")
print(name + "은 어른일까요? " + str(is_adult))
