from collections import Counter, defaultdict, OrderedDict, namedtuple, deque

# Counter 예시
device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])


# defaultdict 예시
coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)


#alma_maters.default_factory = None  # key Error가 다시 발생할 수 있도록 해줌.
alma_maters.default_factory = int  # key Error시 empty integer(0)을 return

print(alma_maters['Rolf'])
print(alma_maters['Anne'])

my_company = 'Telcado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworker[0]])
print(coworker_companies['Rolf'])


# OrderedDict 예시
o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')
o.move_to_end('Jen', last=False)
print(o)
o.popitem()
print(o)

# namedtuple 예시
account = ('checking', 1850.90)

Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 18500.90)
print(account.name)
print(account)

# deque 예시
friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
friends.popleft()

print(friends)
