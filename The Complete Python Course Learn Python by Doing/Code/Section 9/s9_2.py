class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):  # Python2에서는 next로 선언해줘야 함
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()  # generator의 끝에 도착했다고 알려주는 error

    def __iter__(self):
        return self


class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)

my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))

my_numbers = [x for x in [1, 2, 3, 4, 5]]
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])  # gernerator

print(next(my_numbers_gen))