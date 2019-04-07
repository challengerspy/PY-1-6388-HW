# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

spisok=[]
spisok=['яблоко','банан','киви','арбуз']
print(spisok)
i=0
y=1
while i < len (spisok):
    print(f'{y}. ' + '{:>6}'.format(spisok[i]))
    i+=1
    y+=1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok1=list()
spisok2=list()
spisok1=['яблоко','банан','киви','арбуз']
spisok2=['апельсин','лимон','киви','арбуз']
spisok3=[]

spisok3 = []
for el1 in spisok1:
    if el1 in spisok2:
        continue
    else:
        spisok3.append(el1)
spisok1 = spisok3

# alternative
mnoj = set(spisok1).difference(spisok2)

print(spisok1)
print(spisok2)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

spisok1=[]
spisok1=[4,2,6,8,88,100,67]
spisok2=[]
i=0
while i < len(spisok1):
    if int(spisok1[i]) % 2 == 0:
        spisok2.append(int(spisok1[i]/4))
    if int(spisok1[i] % 2 != 0):
        spisok2.append(int(spisok1[i])*2)
    i+=1
print(spisok2)
