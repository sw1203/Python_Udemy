import json

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('cars__json.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string = '[{"name": "Alfo Romeo", "released": 1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])  # 'incorrect_car'가 list 형식으로 되어 있기 때문에 0번째 element의 name을 읽어오는 것
