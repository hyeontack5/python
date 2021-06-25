# 탈출문자, Escape Sequence

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 저는 "오현택"입니다.
print("저는 '오현택'입니다.")
print('저는 "오현택"입니다.')  # 잘 사용 안한다.

# 탈출문자
# \", \' : 문자열 내에서 ", ' 따옴표 처럼 사용할 수 있다.
print("저는 \"오현택\"입니다.")
print("저는 \'오현택\'입니다.")

# \\ : 문자열 내에서 \

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")
