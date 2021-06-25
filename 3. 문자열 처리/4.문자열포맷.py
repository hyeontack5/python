# 문자열포맷

print("a" + "b") # ab
print("a", "b") # a b

# 방법1
print("저는 %d살입니다." % 28)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")
print("저는 %s살입니다." % 28)
print("저는 %s색과 %s색을 좋아합니다." % ("검은", "흰"))

# 방법2
print("나는 {}살입니다." .format(28))
print("저는 {}색과 {}색을 좋아합니다." .format("검은", "흰"))
print("저는 {0}색과 {1}색을 좋아합니다." .format("검은", "흰"))
print("저는 {1}색과 {0}색을 좋아합니다." .format("검은", "흰"))

# 방법3
print("저는 {age}살이며, {color}색을 좋아합니다." .format(age = 28, color = "검은"))
print("저는 {age}살이며, {color}색을 좋아합니다." .format(color = "검은", age = 28))

# 방법4 (python v3.6 이상~)
age = 28
color = "검은"
print(f"저는 {age}살이며, {color}색을 좋아합니다.")
