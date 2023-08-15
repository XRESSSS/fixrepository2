some_string = '''Основная заявленная цель альянса — борьба с «Исламским государством». 
Созданию СДС предшествовали совместные действия курдских отрядов самообороны и части умеренной сирийской
оппозиции (Свободной сирийской армии) в ходе операции «Вулкан Евфрата[en]». Администрация США в рамках новой 
стратегии борьбы с ИГ объявила о поддержке альянса. По состоянию на весну 2016 года, силы СДС насчитывали около 25
тысяч курдских ополченцев и около 5 тысяч арабов[6].
'''

unique_letters = set(some_string)
# print(unique_letters)

letter_counter = dict.fromkeys(unique_letters, 0)

for letter in letter_counter:
    letter_counter[letter] = some_string.count(letter)

letter_counter2 = {}

# for letter in some_string:
#     letter_counter2.setdefault(letter, 0)
#     letter_counter2[letter] += 1
