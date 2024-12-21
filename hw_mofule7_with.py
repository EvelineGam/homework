class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding = 'utf-8') as file:
                file_r = file.read().lower()
                for sym in punctuation:
                    if sym in file_r:
                        file_r = file_r.replace(sym, '')
                words = file_r.split()
            all_words[name] = words
            file.close()
            return all_words

    def find(self, word):
        find_dict = {}
        word = word.lower()
        self.get_all_words()
        for file, words in self.get_all_words().items():
            if word in words:
                find_dict[file] = words.index(word) + 1
            return find_dict

    def count(self, word):
        count_dict = {}
        count = 0
        word = word.lower()
        self.get_all_words()
        for file, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    count += 1
            count_dict[file] = count
            return count_dict

if __name__ == '__main__':

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего







