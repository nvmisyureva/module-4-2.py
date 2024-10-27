#Домашнее задание по уроку "Пространство имен"

x = int(input('Введите число х:'))

def test_function(x):
    y = x * 3
    print(y)
    def inner_function(x):

        if y % 2 == 0:
            print('Я в области видимости функции test_function')
        else:
            print('Увы')

    inner_function(x= 0)
    return y
test_function(x)

print(x)


