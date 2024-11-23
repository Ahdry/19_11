import string

class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем названия файлов в виде кортежа
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем содержимое файла
                    text = file.read().lower()
                    # Убираем пунктуацию
                    text = text.translate(str.maketrans('', '', string.punctuation + ' -'))
                    # Разбиваем текст на слова
                    words = text.split()
                    # Записываем в словарь
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Позиция слова (1-индексация)
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result

# Пример использования
if __name__ == "__main__":
    # Создайте файл test_file.txt с нужным содержимым для тестирования
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))      # Позиция слова
    print(finder2.count('teXT'))     # Количество слов


