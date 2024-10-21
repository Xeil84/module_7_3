import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='UTF-8') as f:
                content = f.read()
                words = content.lower().translate(str.maketrans('', '', string.punctuation)).split()
                all_words[file] = words
        return all_words

    def find(self, word):
        result = {}
        for filename, words in self.get_all_words().items():
            for i, w in reversed(list(enumerate(words))):
                if w == word.lower():
                    result[filename] = i+1
        return result

    def count(self, word):
        result = {}
        for filename, words in self.get_all_words().items():
            result[filename] = words.count(word.lower())
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('teXt')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
