import requests

URL = 'https://script.google.com/macros/s/AKfycbxqfrMNTUBaJgaUYSTJ9nrMfkESayIZoj5kPBpTRQ_Q4EFAUZrl7QYjIsRuri11AQ8bLw/exec'

response = requests.get(URL)
response_json = response.json()
data = response_json['data']

africa_animals = 0

most_expensive_animal = {}
most_expensive_cost_for_month_animal = 0

pass

for animal_info in data:
    amount = animal_info['Amount']
    poisonous = animal_info['Poisonous']
    cost_for_month = animal_info['Cost for month']
    continent = animal_info['Continent']

    if poisonous:
        cost_for_month_poisonous_animal = amount * cost_for_month
        print('Cost for month of poisonous animals -', cost_for_month_poisonous_animal)

    if continent == 'Africa':
        africa_animals += amount
print('Amount of African animals -', africa_animals)

if most_expensive_animal:
    from util_email import send_email, render_html

    result = render_html('templates/zoo_animals.html', most_expensive_animal)

    send_email(
        ['test_hillel_api_mailing@ukr.net'],
        result,
        'mail subject'
    )
