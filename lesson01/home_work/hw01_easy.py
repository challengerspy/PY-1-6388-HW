__author__ = 'Гращенко Игорь Васильевич'



# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

x=input('Введите число:  ')
print(x)
y=str(x)
i=0
while i < len(x):
    print(y[i])
    i=i+1


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a=input('Введите число a: ')
b=input('Введите число b: ')
print(a)
print(b)
c=a
a=b
b=c
print('Число а = ', a)
print('Число b = ', b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age=int(input('Введите ваш возраст : '))
if age >= 18:
    print('Доступ разрешен')
if age<18:
    print('Извините, пользование данным ресурсом только с 18 лет')	
