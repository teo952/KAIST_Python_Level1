key_list = ['구름', '망고', '초고', '동글', '흰둥']
value_list = ['병아리','고양이','강아지','거북이','강아지']

pets = {}
pets2 = {}

for i in range(len(key_list)):
    pets[key_list[i]] = value_list[i]
    
print(pets)

for key in key_list:
    pets2[key] = value_list[key_list.index(key)]
    
print(pets2)


print(range(2,5))
print(list(range(2,5)))

pets2['망고'] = '메롱'
print(pets2)
