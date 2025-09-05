import re


def task_1(string):
    pattern = r'\b(\d{1,2})\s+([А-ЯЁа-яё]+)\s+(\d{4})\b'
    return re.findall(pattern, string)


print(task_1(input('Введите строку: ')))
