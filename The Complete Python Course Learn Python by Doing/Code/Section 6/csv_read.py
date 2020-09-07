file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    """
        title()은 모든 단어의 첫 글자를 대문자로 나머지는 다 소문자로
        capitalize()는 첫 글자만 대문자로 나머지는 다 소문자로
    """
    print(f'{name} is {age}, studying {degree} at {university}.')

sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)