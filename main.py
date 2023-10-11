def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def count_fruit_occurrences(fruit_tuple, target_fruit):
    return fruit_tuple.count(target_fruit)

def count_partial_fruit_occurrences(fruit_tuple, partial_fruit):
    count = 0
    for fruit in fruit_tuple:
        count += fruit.count(partial_fruit)
    return count

def replace_manufacturer(car_tuple, old_manufacturer, new_word):
    return tuple([new_word if manuf == old_manufacturer else manuf for manuf in car_tuple])

# 1
shift = int(input("Введите сдвиг шифрования (целое число): "))
input_text = input("Введите текст для шифрования: ")
encrypted_text = caesar_cipher(input_text, shift)
print("Зашифрованный текст:", encrypted_text)

# 2
fruits = ('apple', 'banana', 'mango', 'banana', 'strawberry-banana')
target_fruit = input("Введите название фрукта для подсчета: ")
occurrences = count_fruit_occurrences(fruits, target_fruit)
print(f"Количество раз, когда {target_fruit} встречается в кортеже:", occurrences)

# 3
partial_fruit = input("Введите часть названия фрукта для подсчета: ")
partial_occurrences = count_partial_fruit_occurrences(fruits, partial_fruit)
print(f"Количество раз, когда {partial_fruit} является частью элемента кортежа:", partial_occurrences)

# 4
manufacturers = ('Toyota', 'Ford', 'Chevrolet', 'Toyota', 'Honda', 'Toyota')
old_manufacturer = input("Введите название производителя для замены: ")
new_word = input("Введите слово для замены: ")
new_manufacturers = replace_manufacturer(manufacturers, old_manufacturer, new_word)
print("Новый кортеж с замененными производителями:", new_manufacturers)




def superset(set1, set2):
    if set1 == set2:
        print("Множества равны")
    elif set1.issuperset(set2):
        print(f"Объект {set1} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4}

superset(set_a, set_b)



class EnglishFrenchDictionary:
    def __init__(self):
        self.dictionary = {}

    def add_word(self, english_word, french_translation):
        self.dictionary[english_word] = french_translation
        print(f'Слово "{english_word}" добавлено в словарь с переводом "{french_translation}".')

    def delete_word(self, english_word):
        if english_word in self.dictionary:
            del self.dictionary[english_word]
            print(f'Слово "{english_word}" удалено из словаря.')
        else:
            print(f'Слово "{english_word}" не найдено в словаре.')

    def search_translation(self, english_word):
        if english_word in self.dictionary:
            print(f'Перевод слова "{english_word}": {self.dictionary[english_word]}')
        else:
            print(f'Слово "{english_word}" не найдено в словаре.')

    def update_translation(self, english_word, new_french_translation):
        if english_word in self.dictionary:
            self.dictionary[english_word] = new_french_translation
            print(f'Перевод для слова "{english_word}" обновлен на "{new_french_translation}".')
        else:
            print(f'Слово "{english_word}" не найдено в словаре.')

    def display_dictionary(self):
        print("Содержимое словаря:")
        for english_word, french_translation in self.dictionary.items():
            print(f'{english_word} - {french_translation}')


dictionary = EnglishFrenchDictionary()

dictionary.add_word("hello", "bonjour")
dictionary.add_word("world", "monde")

dictionary.display_dictionary()

dictionary.search_translation("hello")
dictionary.search_translation("goodbye")

dictionary.update_translation("hello", "salut")

dictionary.display_dictionary()

dictionary.delete_word("world")

dictionary.display_dictionary()





def set_gen(numbers):
    result_set = set()

    for number in numbers:
        if numbers.count(number) > 1:
            result_set.add(str(number) * numbers.count(number))
        else:
            result_set.add(number)

    return result_set

input_numbers = [1, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6]
result_set = set_gen(input_numbers)

print("Исходный список:", input_numbers)
print("Множество с учетом условий:", result_set)

