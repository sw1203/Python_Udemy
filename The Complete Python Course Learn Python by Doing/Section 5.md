# 섹션 5

* [강의제공 자료](https://github.com/tecladocode/complete-python-course/tree/master/course_contents/5_errors/errors_project)

## Error

* Traceback에서는 error가 어디에서 발생했는지를 말해주어 유용

* Error 이해하기

    1. 가장 마지막 줄은 발생한 오류와 설명이 표시
    2. 그 윗줄은 에러가 발생한 코드의 line을 표시
    3. 그 윗줄은 line이 어떠한 function에 포함되어 있는지
    4. 그 윗줄들은 해당 함수가 호출된 위치
    
* Error 발생 시 추천하는 해결과정

    1. 코드 다시 보기
    2. Google, StackOverflow 이용
    3. 코드를 다시 천천히 보면서 값이 어떻게 변화되고 어떻게 컴퓨터에서 실행되는지 생각
    4. 코드를 나눠서 실행해보기 Ex) 함수 단위로
    5. Debugger 사용하기
    
## Errors in python

* IndexError : 인덱스 범위를 벗어나거나 잘못된 인덱스일 경우

* KeyError : 잘못된 Key를 사용하거나 존재하지 않는 Key를 사용한 경우

* NameError : 선언하지 않은 별수를 사용하는 경우 발생

* AttributeError :  속성 이름이 잘못됬거나 없는 속성을 가져오려 하는 경우 발생 
    * 리스트 오브젝트는 intersection이라는 속성을 가지고 있지 않음
    
* NotImplementedError : 파이썬 내장 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용

* RuntimeError : 프로그램 실행 시에 발생하는 에러

* SyntaxError : 문법상의 오류

* IndentationError : 들여쓰기가 잘못되었을 때 발생하는 에러

* TapError : 들여쓰기시 tab과 space를 섞어 사용하는 경우 발생

* DeprecationWarning : Error가 아닌 경고로 더 좋은 방법이 존재한다는 것을 알려줌

## Raising errors in Python

* raise를 이용하여 error를 일으킬 수 있음
* isinstance(A, B) : A의 타입이 B인지 보는 함수 참인 경우 True 거짓의 경우 False

```python
class Garage:
    def __init__(self):
        self.cars = []


    def __len__(self):
        return len(self.cars)


    def add_car(self, car):
        raise NotImplementedError("Error Message")

ford = Garage()
ford.add_car('Fiesta')
print(len(ford))
```


## Creating our own errors

```python
class MyCustomError(Exception):
    """
    docstring
    이 클래스가 무엇인지 method가 무슨 역할을 하는지 적어줌
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

err = MyCustomError('An error happened., 500')
print(err.__doc__) # docstring이 출력된다.
```

## try-except-finally

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f'<Car {self.make} {self.model}'


class Garage:
    def __init__(self):
        self.cars = []


    def __len__(self):
        return len(self.cars)


    def add_car(self, car):
        if not isinstance(car, Car):
            raise ValueError(f"Tried to add a '{car.__class__.__name__}' to the garage, but you can only add 'Car'.")
        self.cars.append(car)


ford = Garage()
fiesta = Car('Ford', 'Fiesta')

try:
    ford.add_car(fiesta)  # 이 함수를 실행하고
except TypeError:  # 이 경우는 typeerror가 발생시 아래 print문 실행 
    print('Your car was not a Car!')
except ValueError:
    print('Something weird happend...')
    raise # traceback이 출력됨
finally:  # try에서 error가 발생하든 안하든 항상 실행된다.
    print(f'The garage now has {len(ford)} cars.')
```

* try-except-else : try를 실행하고 error가 발생하지 않은 경우만 else가 실행

## Debugging 

* Pycharm에서 line number를 클릭하며 breaking point가 된다. 

* Debugging 시 breaking point 바로 윗줄까지 코드가 실행이 된다.

