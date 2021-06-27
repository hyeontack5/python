# 튜플
# 튜플은 리스트와 다르게 내용을 추가 or 삭제할 수 없다.
# 속도가 리스트보다 빠르다

menu = ("김밥", "라면")
print(menu[0])
print(menu[1])

# menu.add("돈까스")
# 오류가 발생한다. 튜플에서는 추가할 수 없다.

name = "오현택"
age = 28
hobby = "코딩"
print(name, age, hobby)

name, age, hobby = "오현택", 28, "코딩"
print(name, age, hobby)

(name, age, hobby) = ("오현택", 28, "코딩")
print(name, age, hobby)
