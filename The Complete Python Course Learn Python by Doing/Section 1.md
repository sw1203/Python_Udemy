

# 섹션 1


## 변수
* snake_case : 변수 선언 시 단어를 _로 이어주는 표현법  ex) friend_age_2
* 변수의 이름은 숫자로 시작할 수 없다.
* 모두 대문자로 선언한 변수는 값을 변경하지 않겠다는 의미이다.  ex) PI =3.14


## 숫자 
* 파이썬에서 나누기 연산( / ) 시 항상 float 형이 반환된다.
* 나누기 연산 시 소수점 이하를 버리고 싶으면 //연산을 사용하면 된다. ex) 8 // 3 -> 2 출력


## String
* String 안에 ' or  "를 포함하는 방법

	``` python
	string_with_quotes = "Hello, it's me."
	another_with_quotes = 'He said "You are amazing!" yesterday.'
	other_with_quotes = "He said \"You are amazing!\" yesterday." # Escaping(문자 앞에 \) 사용
	```
	
* String간의 연산도 가능
	
	``` python
	name = "Jose"
	greeting = "Hello, " + name
	greeting_age = greeting +str(34)
	```
	
* String * Num은 num만큼 string이 반복 ex) "3"*5 -> 33333


## String formatting
* f-string : python 3.6 버전 이상에서만 사용 가능
* 숫자를 문자열로 변환할 필요가 없어짐

```python
age = 34
print(f"U r {age}") # {변수명}
#U r 34

name ="Jose"
greeting = f"How r u, {name}?"
print(greeting)
name = "Bob"
print(greeting)
# How r u, Jose가 두 번 출력 why? f-stirng 연산이 name이 바뀌기 전에 실행

name ="Jose"
final_greeting = "How r u, {}?"
jose_greeting = final_greeting.format(name) # {}에 format(변수)의 변수 값이 들어감
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)
'''
How r u, Jose
How r u, Bob
'''

friend_name ="Jose"
final_greeting = "How r u, {name}?"
jose_greeting = final_greeting.format(name=friend_name) # {name}이라는 곳에 friend_name 값이 들어감
print(jose_greeting)
# How r u, Jose
```


## 데이터 입력
* input("문자열" ) 함수 이용 시 데이터 타입은 String이다.
* 숫자 입력 시 int() 함수를 이용


## Boolean and comparison
* 참 : True , 거짓 : False

``` python
age = 20
is_over_age = age >= 18  # True
is_under_age = age <18 # False
is_twenty = age == 20 # True
'''
= : 할당을 할 때 사용
== : 두 값이 같은지 비교할 때 사용
'''
```

* 변수 할당 시 
	* A and B : A가 True 이면 B를 할당
	* A and B : A가 False이면 A를 할당
	* A or B : A가 True이면 A를 할당
	* A or B : A가 False이면 B를 할당

``` python
x = True and False
print(x) # False

x = 35 and 0
print(x) # 0

x = 0 and 35
print(x) # 0

x = 0 or 35
print(x) # 35

x =  35 or 0
print(x) # 35
```


## 리스트
* 리스트 변수 명은 리스트 내의 element를 잘 표현할 수 있는 변수명을 사용
*  리스트의 element가 많은 경우 아래와 같이 표시하면 읽기 좋다.

``` python
friends = [
	["Rolf", 24],
	["Bob",30],
	["Lee", 26],
	["Park", 27],
	["Koo", 29]
]
```

* .remove(element 값) : element 삭제 

```python
friends = ["Shin", "Park", "Lee"]
friends.remove("Shin") # friends =["Park", "Lee"]
```


## Tuple
*  short_tuple = ("Shin", "Park") 이런 식으로 ()를 통해 선언 
	* ()가 필수 적인 것은 아니다. short_tuple = "Shin", "Park"도 가능하다.
* Tuple은 append로 element를 추가 할 수 없다.
	* Tuple간의 연산으로 데이터 추가 가능 

		``` python 
		friends = ("Shin", "Park", "Lee")
		friends = friends + ("Koo",)
		print(friends) #("Shin", "Park", "Lee", "Koo")
		```

* Tuple은 element를 바꾸고 싶지 않을 때 유용하다.
	* 리스트와 달리 append, remove 불가능


## Set
* 리스트, Tuple과 달리 element가 중복 불가
* element 순서가 일정하지 않다. 

	 ``` python
	 art_friends = {"Shin", "Park"}
	 art_friends.add("Koo")
	 print(art_friends) # {"Koo", "Park", "Shin"} 이런식으로 element 순서가 섞인다.
	 ```

* .remove()로 element를 제거
* A.difference(B) : A set에는 있지만 B set에는 없는 element 반환
* A.symmetric_difference(B) : A set과 B set 중 하나에만 속해 있는 element를 반환 
* A.intersection(B) : A set과 B set에 중복으로 속해 있는 element를 반환 
* A.union(B) : A set과 B set의 모든 element 반환


##  Dictionary
* key 와 value를 저장
* 중복된 key를 가질 수 없고 set과 달리 순서가 바뀌지 않음


## Joining a list
```python
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends) # "구분문자".join(list 명)은 list의 element를 구분문자로 이어서 stirng으로 만들어 줌
print(f"My friends are {comma_separated}.")
# My friends are Rolf, Anne, Chalie.
```
