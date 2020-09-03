# 섹션 2


## 조건문

* if - elif - else


## 반복문
 
* While문
    * 무한 루프에 빠지지 않도록 조심

* For문
    * 다른 언어의 foreach문과 유사하다.
    * range(시작숫자, 종료숫자+1, 증가량) 
        
        ```python
            for index in range(2, 20, 3):
                print(index)  # 2 5 8 11 14 17
        ```


## Destructuring syntax

* 사용시 프로그램의 가독성이 좋음

``` python
    friends =[("Shin", 26), ("Kim", 27), ("Park", 28)]
    
    for name, age in friends: # 첫 번째 element는 name에 두 번째 element는 age로 이것이 destructuring syntax
        print(f"{name} is {age} years old.")
```


## Iterating over dictionaries

* for i in A: i는 A의 키들이 반복된다.
* for i in A.values(): i는 A의 값들이 반복된다.
* for name, age in friends_ages.items(): name에는 key가 age에는 key에 해당하는 값이 반복된다.


## Break and Continue

* 반복문에서 break는 반복문을 종료하지만 continue는 continue 아래의 내용을 skip하고 다음번 반복을 수행


## for - else

* for과 else가 같은 레벨에 존재 시 else문은 for문이 중간에 break를 만나지 않고 완벽하게 실행되면 실행하라는 의미

```python
    for n in range(2,10):
        for x in range(2,n):
            if n%x == 0:
                print(f"{n} equals {x} * {n//x}")
                break
        else:
            print(f"{n} is a prime number.")
```


## List slicing

* A[2:4] -> A의 2번째 element부터 4-1 = 3 번째 element까지
* A[-3:] -> A의 len이 5일때 5-3 = 2 번쨰 element부터 끝까지


## List Comprehensions

``` python
    numbers = [0, 1, 2, 3, 4]
    double_numbers = [number * 2 for number in numbers] 
    
    """    
        list comprehension으로 number * 2를 리스트에 추가할 것 이고 number는 numbers의 element라는 의미 
    """

    friends_ages = [22, 31, 35, 37]
    age_string = [f"My friends is {age} years old." for age in friend_ages]
```

* .title() : 모든 단어의 시작은 대문자로 나머지는 소문자로 바꿔주는 역할
* capitalize() : 문자열의 첫번째 문자는 대문자로 변환하고 나머지는 소문자로 변환


## Comprehensions with conditionals

``` python
    ages = [22, 35, 27, 21 ,20]
    odds = [age for age in ages if age % 2 == 1]
    
    """
        comprehensions with conditionals로 age를 리스트에 추가할 것이고 age는 ages의 element이고 age가 홀수인 경우만 추가할 것이다라는 의미
    """
```


## Splitting Comprehensions

* Comprehension이 많아지면 가독성에 문제가 생길 수 있어 다음과 같이 나누는 것이 좋다.

```python
    friends = ["Rolf", "ruth", "charlie", "Jen"]
    guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

    present_friends = [
        name.title()  # list에 추가하고자 하는 것
        for name in guests  # 어떤 리스트의 element를 반복할 것인지
        if name.lower() in [f.lower() for f in friends]   # if 조건문
    ]
```

* 예시에서 [f.lower() for f in friends]은 따로 리스트를 선언해 주고 한 줄로 작성하는 것이 좋다.


## zip 함수

* 여러 리스트의 element들을 순서대로 튜플로 묶어줌
* list[zip()] , dict[zip()] 이런 식으로 많이 사용
* zip 함수는 다른 리스트의 element와 매치가 되지 않는 element들은 무시한다.

``` python
    friends = ["Rolf", "Bob"]
    time_since_seen = [3, 7]

    long_timers = list(zip(friends, time_since_seen, [1, 2, 3]))  # [("Rolf", 3, 1), ("Bob", 7, 2)]
```


## enumerate 함수

* 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
* enumerate(A, start =1) -> 순서를 0이 아닌 1부터 시작

```python
    friends = ["Rolf", "John", "Anna"]

    for counter, friend in enumerate(friends):
        print(counter)  # 0, 1, 2
        print(friend)  # Rolf, John, Anna

    list(enumerate(friends))  # [(0, "Rolf"), (1, "John"), (2, "Anna")]
```


## 함수

* def greet() : greet이라는 함수를 선언하겠다는 의미
* 함수는 미리 선언하고 나서 그 다음에 사용 가능하다.
* 함수를 여러 개 선언 시 함수간 두 줄을 띄우는 것을 추천한다.


## Argument

* Argument는 함수로 전달해 주기위한 값
* Parameter는 함수 내에서 값을 받는 변수 


## Default parameter value

* 파라미터의 값을 미리 설정해 놓는 것으로 함수 호출 시 값을 넘겨주지 않으면 default 값이 넘어간다.

```python
     def add(x, y=3):
          total = x + y
          return total

     print(add(5))  # 8
     print(add(5,1))  # 6
```

* print(1, 2, 3, 4, 5, sep=" - ") 을 실행하면 1 - 2 - 3 - 4 - 5가 출력된다.


## Lambda 함수

* Lambda 함수는 입력을 받고, 소량의 처리를 수행하고, 반환하는데 사용

``` python
     def divide(x, y):
          return x / y
     
     """
          위 함수를 람다식으로 표현하면
          divide = lambda x, y: x / y 
          lambda 파라미터 : 수행할 내용
     """
```


## First Class function

* 변수에 함수를 할당할 수 있으며, 인자로써 다른 함수에 전달하거나 함수의 리턴 값으로 사용 가능

```python
     def square(x):
          return x * x
     
     f = square
     print(f(5))  #  25
```
