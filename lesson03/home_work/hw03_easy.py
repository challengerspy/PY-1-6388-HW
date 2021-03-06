# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass

def my_round(number, ndigits):
    a=str(number)
    dot_index=a.find('.')
    mant=a[dot_index+1:]
    if len(mant) < ndigits:
        return number
    end_mant=int(mant[ndigits])
    start_mant=int(mant[:ndigits])
    if end_mant >= 5:
        start_mant+=1
    return float(f'{int(number)}.{start_mant}')

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def to_digit(input):
    a=input
    while a > 0:
        yield a % 10
        a //= 10
    
def lucky_ticket(ticket_number):
    if 100000 < ticket_number <= 1000000:
        left= ticket_number % 1000
        right= ticket_number // 1000
        if (sum(to_digit(left))) == (sum(to_digit(right))):
            return True
        else:
            return False
    raise Exception('bad number')
    
print(lucky_ticket(123006))
try:
    print(lucky_ticket(12321))
except Exception as exc: 
    print(exc)
print(lucky_ticket(436751))


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
