"""
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку
здійснюється за механізмом
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення,
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
# ваш код нижче !!!!!!!! вище нічого не змінюємо
full_name = 'Микола Савчук'
students[full_name] = {
    'Пошта': 'Mykola@gmail.com',
    'Вік': 24,
    'Номер телефону': '+380943254789',
    'Середній бал': 85
}

honor_students = []
for student, info in students.items():
    if info['Середній бал'] > 90:
        honor_students.append({'Ім’я та прізвище': student, 'Середній бал': info['Середній бал']})
print('Excellent students:', honor_students)

def average_grade(students):
    count = 0
    total_grade = 0

    for info in students.values():
        total_grade += info['Середній бал']
        count += 1

    average_grade = total_grade / count
    return average_grade
print('Average grade of group:', average_grade(students))

for student, info in students.items():
    if info['Номер телефону'] == None:
        print({'Ім’я та прізвище': student, 'Parents number': '+380943212223'})
