# person_name = 'Alex'
# person_age = 16
#
# person = {
#     'person_name': 'John',
#     'ages': 20,
#     'hobbies': [
#         'soccer',
#         'tennis'
#     ]
# }
#
# animal = {'bread': 'cally'}
#
# person1 = {
#     'person_name': 'Alex',
#     'ages': 15,
#     'hobbies': [
#         'soccer',
#         'tennis'
#     ]
# }
# ageperson = person1['ages']
# print(ageperson)
#
from main import person

person2 = {
    'person_name': 'Alex',
    'surname': 'Denis',
    'ages': 15,
    'best_friend': {
        'ages': 11,
        'hobbies': [
            'soccer',
            'tennis'
        ]
    },
    'classes': None
}
age_of_the_best_friend = person2['best_friend']['ages']
print(age_of_the_best_friend)

# READ
person_2_name = person2['person_name']
person_2_surname = person2.get('surname')
person_2_car = person2.get('car', 'bycicle')
person_2_car2 = person2.get('car') or 'bycicle'
person_2_classes: list[str] = person2.get('classes', []) or []

for key, values in person2.items():
     pass



pass