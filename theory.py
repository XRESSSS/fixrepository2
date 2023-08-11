# обробка помилок
first_number = 55
second_number = 1

# if second_number != 0:
#     div = first_number / second_number


# try:  # в даному блоці коду має бути мінімум коду, тільки той, який поже викликати помилку
#     division = first_number / second_number
# except ZeroDivisionError as error:  # блок відпрацьовує, якщо зазначений тип помилки стався
#     print(error)
#     division = 0
# except (ValueError, TypeError):
#     print('Сталися або ValueError, або TypeError помилки')
#     division = None
# else:  # виконається, якщо помилок не буде
#     print('Все пройшло штатно')
# finally:  # буде виконано в будь-якому випадку
#     print("Ви навчилися працювати з блоками try-except")
#
# print(division)


# def division_function(divisible: int | float, divisor: int | float) -> float:
#     try:
#         fraction = divisible / divisor
#         return fraction
#     except ZeroDivisionError as error:
#         fraction = 0
#     finally:
#         fraction = 0
#
#     return fraction
#
# print(division_function(5, 0))


# set
# створення сету
# В СЕТ МОЖУТЬ ПОПАСТИ ТІЛЬКИ НЕЗМІННІ ОБЄКТИ!!!

some_list = [5, 'jkhg']

var1 = set()

# або
list_two_elements = ['aaa', 'aaa']
var2 = set(list_two_elements)

# або
var3 = {2, 5, True}

# приклад передачі списку в сет
# list_city = input('>>>>>>>>> ').title().split()
# print(list_city)
# unique = set(list_city)
# print(unique)
#
# довжина сету
# print(len(unique))

# додавання 1 елементу
var1.add(5)

# додавання кількох елементів
var1.update('jhfaahb')
var1.update(list_two_elements)
print(var1)

# перетворення сету в список
new_list = list(var1)
print(new_list)

# видалення елементу - при його відсутності помилка не виникає
var1.discard(5555)

# видалення елементу - при його відсутності помилка виникає
var1.remove(5)
#
# видалення випадкового елементу. метод повертає видалений елемент
temp = var1.pop()
print(temp)
print(var1)
#
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# робота з множинами, результат можна записати в окрему змінну, наприклад і = set1 & set2
# вихідні множини не міняються
# спільні елементи для двох множин
print('пересічення множин', set1 & set2)
print('пересічення множин', set1.intersection(set2))
common = set1 & set2
print(common)

# всі елементи всіх множин
print('об\'єднання', set1 | set2)
print('об\'єднання', set1.union(set2))

# залишаються тільки ті елементи першої множини, яких немає в другій множині
print('різниця', set1 - set2)
#
# елементи, які є відмінними для різних множин
print('відмінність', set1 ^ set2)


def a_b_check(string: str) -> bool:
    """a b
    aaaaaaaaaabbbbbbbb - True
    aaaaaaaaaaaaaaaa - True
    bbbbbbbb - True
    aaaaabbbab - False
    """
    if len(set(string)) == 1:
        return True

    cleaned_string = string.rstrip('b')
    if 'b' in cleaned_string:
        return False

    return True



# dict
# словник - це структура даних, яка складається з незмінного ключа та будь-якого значення
# значенням може бути інший словник
# словники бажано створювати для зберігання інформації за її змістом чи походженням
person = {
    'name': 'Igor',
    'age': 18,
}

dict_creation_2 = dict()
dict_creation_3 = dict(city='Odesa', village='Myrne')
dict_creation_4 = {}
dict_creation_5 = dict.fromkeys(set1, True)  # другий аргумент буде переданий як значення для всіх
# ключів новоствореного словника, інакше None
print('from keys', dict_creation_5)

#  доступ до значень словника здійснюється по ключам наступним чином:
print(person['name'])

# при відсутності ключа виникне помилка KeyError
# print(person[55])
#
# для уникнення помилки використовуємо синтаксис, причому можна опціонально вказати, що повернути,
# якщо такого ключа немає
# цей прийом НЕ змінює вихідний словник
print(person.get(55, 'Igor2'))
print(person.get("name"))

# створення копії словника
second_dict = person.copy()

# для уникнення помилки використовуємо синтаксис, причому можна опціонально вказати, що повернути,
# якщо такого ключа немає
# цей прийом ЗМІНЮЄ вихідний словник
print(person.setdefault(99999999, 9))
print(person)
person.popitem()
print(person)
# перевірити адреси, де зберігаються дані словників
print('id1', id(person))
print('id2', id(second_dict))

# для перезапису або добавлення значення словника за ключем використовуємо синтаксис
# створить нову пару ключ-значення
person['hobby'] = 'tennis'
# змінить раніше записані дані
person['age'] = 55
#
print(person)
# для уникнення помилки використовуємо синтаксис, причому можна опціонально вказати,
# що повернути, якщо такого ключа немає
# цей прийом НЕ змінює вихідний словник
#######################################
# ПРАКТИКА
# порахувати, скільки яких букв в стрічці
#
# вихідна стрічка
my_string = 'lkdsjfghdfgkdfhgjkldfjslk;ghdf hgdfklghdfkl ghdfjkl;hdfkjlhgkdfjhgkjlhdfghkdfjhgfdkjghfdjklhg kldfh '
# за допомогою сета вибираємо унікальні літери
unique = set(my_string)
# на основі сету створюємо словник, де ключами будуть літери, а початковими значеннями - 0
# (початкове значення при лічбі)
dict_counter = dict.fromkeys(unique, 0)

print(dict_counter)
# for item in dict_counter:
#     print(item)

for key, value in dict_counter.items():
    print(key, value)
    dict_counter[key] = my_string.count(key)
    print(key, dict_counter[key])
    print('*' * 20)

print(dict_counter)




#
# обхід словника - за замовченням по ключах
print(dict_counter.items())
dict_counter.keys() #- повертає особливий список ключів, які за допомогою функції list
# можна перетворити на звичайний список
n = list(dict_counter.keys())
print(n)
# dict_counter.values() #- повертає особливий список значень, які за допомогою функції list
# можна перетворити на звичайний список
m = list(dict_counter.values())
#
# # наповнюємо словник - кожна літера стрічки вже є в словнику, і тому може бути використана як ключ в словнику
# # for letter in my_string:
# #     dict_counter[letter] += 1
#
# for key in dict_counter:
#     dict_counter[key] = my_string.count(key)
#
# print(dict_counter)
#
# варіанти обєднанння словників
dict3 = {**person, **dict_creation_3}
dict3 = dict_creation_3 | person  # пайтон 3.9
print(dict3)
#
# видалення пари ключ-значення при доступі по ключу
del dict3["age"]
print('del', dict3)
#
# видалення елемента по ключу, видалене значення можна записати в змінну
c = dict3.pop('hobby')
print('pop', dict3, 'deleted', c)
#
# видалення останнього елемента (пари), видалене значення можна записати в змінну
d = dict3.popitem()
print('popitem', dict3, 'deleted', d)
#
# повна очистка словника, назва змінної та тип даних залишаються
dict3.clear()
print(dict3)
