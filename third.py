#Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
dictionary = {}
dictionary = \
    {
        'Привет': 'Добрый день!', 
        'привет':'Добрый день!',
        'Как тебя зовут?': 'Меня зовут Алекс',
        'Какая сейчас пора года?': 'Сейчас зима',
        
    }

phrase = input(' Введите фразу: ') 
if phrase in dictionary:
    print(dictionary[phrase])
else:
    print('э-э-э Не понимаю тебя, напиши "Привет"')
