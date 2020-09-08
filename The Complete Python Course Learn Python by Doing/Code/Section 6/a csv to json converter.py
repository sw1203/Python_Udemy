import json

json_list = []
csv_file = open("csv_file.txt", "r")
csv_lines = [line for line in csv_file.readlines()]
csv_file.close()

for line in csv_lines:
    club, city, country = line.strip().split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
        }
    json_list.append(data)

json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)
json_file.close()
