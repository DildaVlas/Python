def task_1(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 3 != 0:
            count += 1
    return count


def task_2(n):
    min_digit = None
    for digit in str(n):
        digit = int(digit)
        if digit % 2 != 0:
            if min_digit is None or digit < min_digit:
                min_digit = digit
    return min_digit


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def task_3(n):
    sum_digits = sum(int(digit) for digit in str(n))
    product_digits = 1
    for digit in str(n):
        product_digits *= int(digit)

    special_divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            if gcd(i, sum_digits) == 1 and gcd(i, product_digits) != 1:
                special_divisors.append(i)
    return sum(special_divisors)


try:
    inp = int(input("Введите номер задания (1, 2 или 3): "))

    if not 1 <= inp <= 3:
        raise ValueError

    arg = int(input("Введите аргумент: "))

    match inp:
        case 1:
            print(task_1(arg))
        case 2:
            print(task_2(arg))
        case 3:
            print(task_3(arg))
except ValueError:
    print("Неправильный аргумент, или номер задания.")

"""
1. Класс int
Класс int в Python представляет целые числа. Он поддерживает арифметические, побитовые операции и имеет методы, такие как bit_length(), conjugate(), атрибуты denominator и numerator.

2. Циклы в Python
for: Итерация по последовательностям:
for i in range(5):
    print(i)
    
while: Повторение блока кода, пока условие истинно:
i = 0
while i < 5:
    print(i)
    i += 1
    
Управление циклами:
break: Прерывание цикла.
continue: Переход к следующей итерации.
else: Блок кода, выполняемый при нормальном завершении цикла.

3. Функции в Python
Описание:
def function_name(parameters):
    # Блок кода
    return result

Вызов:
result = function_name(arguments)
Возвращаемое значение по умолчанию
None (если нет return).
"""
