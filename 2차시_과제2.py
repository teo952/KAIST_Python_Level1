name = str(input("이름을 입력하세요  : "))
age = str(input("나이를 입력하세요 : "))

# 이름을 10자리에서 중앙 정렬
formatted_name = f"{name:^10}"

# 나이를 5자리에서 오른쪽 정렬
formatted_age = f"{age:>5}"

print(f"{formatted_name}")
print(f"{formatted_age}")
print(f"{formatted_age:>15}")

print("{:^10}".format(name))
print("{:>5}".format(age))

print(f"제 나이는 {age:>5} 입니다.")