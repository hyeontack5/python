# 가변인자

# 가변인자 적용 X
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
  # 원래 print를 출력하면 줄바꿈이 되지만, \
  # end=" " 을 해주면 print를 출력하고 끝에는 " " 이걸로 준다는 뜻이다.
  print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ")
  print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("오현택", 28, "Python", "C", "", "", "")

# 가변인자 적용 O
def profile(name, age, *language):
  # 원래 print를 출력하면 줄바꿈이 되지만, \
  # end=" " 을 해주면 print를 출력하고 끝에는 " " 이걸로 준다는 뜻이다.
  print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ")
  for lang in language:
    print(lang, end=" ")
  print() # 줄바꿈을 위해서 사용한다.

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("오현택", 28, "Python", "C")