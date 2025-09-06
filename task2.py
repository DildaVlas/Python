import re
from collections import Counter


def find_common_word_in_sentences(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    if not sentences:
        return "В тексте нет предложений."

    word_counts = [Counter(re.findall(r'\w+', sentence.lower())) for sentence in sentences]

    common_words = set(word_counts[0].keys())
    for words in word_counts[1:]:
        common_words.intersection_update(words.keys())

    if not common_words:
        return "Нет слова, встречающегося в каждом предложении."

    return list(common_words)[0]


def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# Пример использования
text = read_text_from_file('data/text.txt')
common_word = find_common_word_in_sentences(text)
print(common_word)
