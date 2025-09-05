import random


def task_1(s):
    chars = list(s)
    random.shuffle(chars)
    return ''.join(chars)


def task_2(s):
    uppercase_chars = [char for char in s if char.isupper()]
    return uppercase_chars == uppercase_chars[::-1]


def task_3(s):
    words = s.split()
    sorted_words = sorted(words, key=len)
    return ' '.join(sorted_words)


try:
    inp = int(input("Введите номер задания (1, 2 или 3): "))

    if not 1 <= inp <= 3:
        raise ValueError

    arg = input("Введите аргумент: ")

    match inp:
        case 1:
            print(task_1(arg))
        case 2:
            print(task_2(arg))
        case 3:
            print(task_3(arg))
except ValueError:
    print("Неправильный аргумент, или номер задания.")
