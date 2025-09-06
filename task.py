def build_family_tree(n, parent_pairs):
    tree = {}
    for child, parent in parent_pairs:
        tree[child] = parent
    return tree


def calculate_heights(tree):
    heights = {}
    for child in tree:
        if child not in heights:
            current = child
            height = 0
            while current in tree:
                current = tree[current]
                height += 1
            heights[child] = height
    return heights


n = int(input("Введите количество элементов в генеалогическом древе: "))
parent_pairs = []
for _ in range(n - 1):
    child, parent = input("Введите имя потомка и имя родителя(Alexei Peter): ").split()
    parent_pairs.append((child, parent))

tree = build_family_tree(n, parent_pairs)
heights = calculate_heights(tree)

# Добавляем родоначальника в словарь высот
root = [child for child in tree if child not in tree.values()][0]
heights[root] = 0

# Выводим результат в лексикографическом порядке
for name in sorted(heights.keys()):
    print(f"{name} {heights[name]}")


"""
1. Методы словарей в Python
keys(): Возвращает список всех ключей в словаре.
values(): Возвращает список всех значений в словаре.
items(): Возвращает список всех пар ключ-значение в словаре.
get(key, default=None): Возвращает значение для указанного ключа. Если ключ не найден, возвращает значение по умолчанию.
pop(key, default=None): Удаляет указанный ключ и возвращает его значение. Если ключ не найден, возвращает значение по умолчанию.

2. Способы задать словарь
Пустой словарь:
d = {}
Словарь с элементами:
d = {'a': 1, 'b': 2, 'c': 3}

Словарь с использованием функции dict():
d = dict([('a', 1), ('b', 2), ('c', 3)])

Словарь с использованием генератора словарей:
d = {x: x**2 for x in range(5)}

Словарь с использованием функции zip():
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
"""
