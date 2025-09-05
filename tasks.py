from collections import Counter


def average_ascii_weight(s):
    return sum(ord(char) for char in s) / len(s)


def task_1(strings):
    return sorted(strings, key=average_ascii_weight)


def task_2(strings):
    sorted_strings = sorted(strings, key=len)
    median_strings = []
    while sorted_strings:
        median_index = len(sorted_strings) // 2
        median_string = sorted_strings.pop(median_index)
        median_strings.append(median_string)
    return median_strings


def quadratic_deviation(s):
    max_ascii = max(ord(char) for char in s)
    n = len(s)
    deviation_sum = 0
    for i in range(n // 2):
        deviation = abs(ord(s[i]) - ord(s[n - i - 1]))
        deviation_sum += (max_ascii - deviation) ** 2
    return deviation_sum


def task_3(strings):
    return sorted(strings, key=quadratic_deviation)


def quadratic_deviation_most_common(strings):
    all_chars = ''.join(strings)
    most_common_char = Counter(all_chars).most_common(1)[0][0]
    deviation_sum = 0
    for s in strings:
        char_count = Counter(s)
        deviation = char_count[most_common_char] - char_count[most_common_char]
        deviation_sum += deviation ** 2
    return deviation_sum


def task_4(strings):
    return sorted(strings, key=lambda s: quadratic_deviation_most_common([s]))


try:
    inp = int(input("Введите номер задания (1, 2, 3 или 4): "))

    if not 1 <= inp <= 4:
        raise ValueError

    arg = input("Введите аргумент: ")

    match inp:
        case 1:
            print(task_1(arg))
        case 2:
            print(task_2(arg))
        case 3:
            print(task_3(arg))
        case 4:
            print(task_4(arg))
except ValueError:
    print("Неправильный аргумент, или номер задания.")

"""
1. Методы строк в Python
split(sep=None, maxsplit=-1): Разбивает строку по разделителю sep и возвращает список подстрок. maxsplit указывает максимальное количество разбиений.
join(iterable): Объединяет элементы итерируемого объекта в строку с разделителем.
strip(chars): Удаляет указанные символы chars с начала и конца строки. По умолчанию удаляет пробелы.
replace(old, new, count=-1): Заменяет все вхождения подстроки old на new. count указывает максимальное количество замен.
find(sub, start=0, end=-1): Возвращает индекс первого вхождения подстроки sub в строке. Если подстрока не найдена, возвращает -1.

2. Особенности работы с индексами в строке на Python
Индексация: Строки в Python индексируются с нуля. Первый символ строки имеет индекс 0, последний — -1.
Срезы: Строки поддерживают срезы, которые позволяют извлекать подстроки.
Неизменяемость: Строки в Python являются неизменяемыми. Это означает, что после создания строки её содержимое нельзя изменить.
Итерация: Строки можно итерировать с помощью цикла for.
Длина строки: Длина строки можно получить с помощью функции len().
"""