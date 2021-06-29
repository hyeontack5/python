# 기본값

# 문장이 너무 길어 지면 "\" 역슬래쉬를 사용해서 줄 바꿈을 할 수 있다.
def profile(name, age, main_lang):
  print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
  .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("오현택", 28, "자바")

# 같은 학교 같은 반 같은 수업

# 함수의 매개변수에 default 값을 줄 수 있다.
def profile_class(name, age=17, main_lang="파이썬"):
  print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
  .format(name, age, main_lang))

profile_class("유재석")
profile_class("오현택")

