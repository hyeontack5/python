# 키워드값

def profile(name, age, main_lang):
  print(name, age, main_lang)

# 키워드를 이용해서 함수를 호출하게 되면 \ 
# 순서에 상관없이 그 해당 키에 값으로 들어가게 된다.
profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=28, name="오현택")