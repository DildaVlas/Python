def task_1(s):
    max_count = 0
    current_count = 0
    for char in s:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count


def task_2(s):
    words = s.split()
    min_num = None
    for word in words:
        if word.isdigit():
            num = int(word)
            if min_num is None or num < min_num:
                min_num = num
    return min_num


def task_3(s):
    max_count = 0
    current_count = 0
    for char in s:
        if char.isdigit():
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count


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
