# 섹션 4

## Object-Oriented Programming

* python에서 __함수명__은 dunder function이라 부르는 특별한 함수이다.
    * [참고 자료](https://corikachu.github.io/articles/python/python-magic-method)

```python
    class Student:
        def __init__(self, new_name, new_grades): # self is blank object
            self.name = new_name
            self.grade = new_grades
        

        def average(self):
            return sum(self.grades) / len(self.grades)

    student_one = Student('Rolf Smith', [70, 88, 90, 99])
    print(student_one.name)  # Rolf Smith
    print(student_one.average())  # 86.75 Student.average(student_one)도 가능
```

## Class and Objects

* 위의 예시에서 name, grade는 객체의 속성(property)라 부른다.
* class 내의 함수는 method라 부른다.
* object를 argument로 함수에 넘겨줄 수 있다.
* [참고자료](https://wikidocs.net/28)


## Built-in functions

* 정의할 필요없이 파이썬에 내장되어 있는 함수
    * [official document](https://docs.python.org/3.7/library/functions.html)
    

## Magic Method

```python
    class Garage():
        def __init__(self):
            self.cars = []
        

        def __len__(self):
            return len(self.cars)
        

        def __getitem__(self, i):
            return self.cars[i]
        

        def __repr__(self):
            return f"<Garage {self.cars}>"


        def __str__(self):
            return f"Garage with {len(self)} cars"

    ford =Garage()
    ford.cars.append('Fiesta')
    ford.cars.append('Focus')
    
    print(len(ford))  # 2
    print(ford[0])  # Fiesta Garage.__getitem__(ford, 0)과 같음
    print(ford)  # Garage with 2 cars

```

## 상속 

* 상위 클래스의 속성과 메소드를 하위 클래스에서 사용할 수 있게 하는 것
* 하위 클래스가 상위 클래스의 method 호출 가능 그러나 상위 클래스가 하위 클래스에만 정의된 메소드 호출 불가
```python
    class Student:
        def __init__(self, name, school):
            self.name = name
            self.school =school
            self.marks = []

        def average(self):
            return sum(self.marks) / len(self.marks)

    
    class WorkingStudent(Student):  # WorkingStudent는 Student의 자식 class
        def __init__(self, name, school, salary):
            super().__init__(name, school)  # super는 부모 클래스
            self.salary = salary
        
        def weekly_salary(self):
            return self.salary * 37.5

    rolf = WorkingStudent('Rolf', 'MIT', 15.50)
    print(rolf.salary)
    rolf.marks.append(57)
    rolf.marks.append(99)
    print(rolf.average())
```

## @property decorator

* getter와 같은 역할

```python
    class Student:
        def __init__(self, name, school):
            self.name = name
            self.school =school
            self.marks = []

        def average(self):
            return sum(self.marks) / len(self.marks)

    
    class WorkingStudent(Student):  # WorkingStudent는 Student의 자식 class
        def __init__(self, name, school, salary):
            super().__init__(name, school)  # super는 부모 클래스
            self.salary = salary
        
        @property     
        def weekly_salary(self):
            return self.salary * 37.5

    rolf = WorkingStudent('Rolf', 'MIT', 15.50)
    print(rolf.weekly_salary)  # 581.25 @property 때문에 weekly_salary()라고 안해도 됨
```

## @classmethod and @staticmethod

* Object를 생성할 필요없이 class로 접근가능
* @staticmethod 보다 @classmethod 사용하는 것을 추천한다.
* @classmethod에는 self대신 cls라는 파라미터를 사용한다. cls는 object가 아닌 class를 받는다. self는 object를 받는다.
* [참고자료](https://wikidocs.net/21054)

```python
class FixedFloat:
    def __init__(self, amount):
        self.amount == amount


    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    
    @staticmethod
    def from_cum(value1, value2):
        return FixedFloat(value1 + value2)

new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)  # <FixedFloat 20.36>

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro.from_sum(16.758, 9.999)  # 수행 후 FixedFloat object가 반환된다
print(money)  # <FixedFloat 26.76>
```

```python
class FixedFloat:
    def __init__(self, amount):
        self.amount == amount


    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    
    @classmethod
    def from_cum(cls, value1, value2):
        return cls(value1 + value2)

new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)  # <FixedFloat 20.36>

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro.from_sum(16.758, 9.999)  # @classmethod를 사용함으로 Euro class가 cls로 넘어간다
print(money)  # <Euro €26.76>

```
