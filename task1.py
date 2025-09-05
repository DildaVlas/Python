# Чтение списка строк с клавиатуры
def task_1():
    strings = []
    print("Введите строки (для завершения введите 'stop'):")
    while True:
        inp = input()
        if inp.lower() == 'stop':
            break
        strings.append(inp)

    # Упорядочивание строк по длине
    return sorted(strings, key=len)


# Вывод упорядоченного списка строк
print("Упорядоченный список строк:")
for s in task_1():
    print(s)
