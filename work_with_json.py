import json

location = {
    'area_name': 'Одеська область',
    'population': 2_220_006,
    'image': '★'
}

json_str = json.dumps(location)

dict_from_json = json.loads(json_str)

# with open('data.json', mode='w') as file:
#     json.dump(location, file, indent=4)

with open('data.json', mode='r') as file:
    data_from_file = json.load(file)

pass
