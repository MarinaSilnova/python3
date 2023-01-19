#Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи

def fibonacci(e):
    number1 = 1 
    number2 = 1
    for i in range(e):
        yield number1
        number1 = number2
        number2 = number1 + number2
n = int(input('Введите число N: '))
fib = list(fibonacci(n))
print(fib)
data = open('test.txt', mode ='w', encoding ='utf-8')
text = data.writelines(str(fib))
data.close()