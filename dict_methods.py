from pprint import pprint

class_info = {
    'name': '1C',
    'quantity_of_pupils': 32,
    'average_score': 11.3,
    'class_teacher': 'Валентина Ивановна',
    'hobbies': [
        'chess',
        'soccer',
    ],
    'furniture': {
            'type': 'wardrobe',
            'cost': 1000.00,
    },
    'list_of_pupils': [
        'Baran'
        'Baran2'
        'Baran3'
        'Baran4'
        'Baran5'
        'Baran6'
    ]
    # 'major_pupil': 'Baran',
}

quantity_pupils = class_info['quantity_of_pupils']
print(quantity_pupils)
cost = class_info['furniture']['cost']
print(cost)

# major_pupil = class_info.get('major_pupil', class_info['list_of_pupils'][0])
major_pupil = class_info.get('major_pupil', '')
# print(major_pupil)

# print(major_pupil + 'ASALAMELEYKUM')

pprint(class_info, width=50)

class_info.setdefault('major_pupil', 'Max')
# pprint(class_info)

class_info['rank'] = 'brilliant'
# pprint(class_info)

class_info['rank'] = 'wooden'
# pprint(class_info)


# for key in class_info:
#     print(key, class_info[key])
#     print('*' * 20)
# print(class_info.items())

pair1 = 'name', '1C', 456
key, value, *other_data = pair1

print(value)
print(pair1)
pair2 = 'name', '1C'
key2, value2 = pair2
print(pair2)
tuple_try = (5,)
print(tuple_try)


for key, value in class_info.items():
    print(key, value)
    print('*' * 20)

del class_info['rank']

our_major_pupil = class_info.pop('major_pupil')
print(f'Thank you, {our_major_pupil}, you was the best baran')

# жоский кринж, таким не пользуемся
# last_pair = class_info.popitem()
# print(last_pair)

class_info.clear()

print(class_info)
