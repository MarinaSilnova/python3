# В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
data = open('test2.txt', encoding='utf-8')
text = data.readlines()
data.close()
letter = input('ВВедите букву: ')
for i in range(len(text)):
    fruit = text[i]
    if fruit[0] == letter:
        print(fruit, end= '')
   
