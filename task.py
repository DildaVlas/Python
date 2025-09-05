def count_unique_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)


# Пример использования
raw_numbers = [1, 2, 3, 2, 1]
print(count_unique_numbers(raw_numbers))  # Вывод: 3
