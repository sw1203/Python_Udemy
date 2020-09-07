# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

friends = input('Enter three friends names, separated by commas (no spaces, please): ').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]  # .strip() 함수는 주어진 문자열에서 양쪽 끝에 있는 공백과 \n 기호를 삭제

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)  # 2 set에 중복으로 속해있는 element들을 반환

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
