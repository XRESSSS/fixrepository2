# list_similar_elements = [5, 55555555555, 5, 5, 66, 'djsahdjklsahdkjsah']
# # set
# # только не сменные объекты попадают в сет
# set1 = set()
# print(set1)
#
# set2 = set(list_similar_elements)
# print(set2)
# print(len(set2))
#
# set3 = {6, 5, 'dsadsa', 88}
# print(set3)
#
# print(set('dasddfghjkl;zxcvbnm'))
#
# unique_letters = set('asdfghjkbvc')
# unique_letters.add('R')
# print(unique_letters)
#
# unique_letters.update('QWERTY')
# unique_letters.update(list_similar_elements)
# print(unique_letters)
#
# # print(list(unique_letters))
#
# unique_letters.discard(4444444)
# unique_letters.discard('Q')
# print(unique_letters)
#
# unique_letters.remove('R')
#
# print(unique_letters.pop())

set1 = {1, 2, 3}
set2 = {3, 4, 5}
# спильни елементы для двоих множин
print('пересечение чисел', set1 & set2)
print('пересечение чисел', set1.intersection(set2))

# все елементы всех чисел

