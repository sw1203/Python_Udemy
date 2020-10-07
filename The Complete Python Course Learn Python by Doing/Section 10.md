# 섹션 10
* [실습코드](https://github.com/sw1203/Python_Udemy/tree/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2010)

## mutability
* [참고자료](https://dpdpwl.tistory.com/82)
* 변경 가능한 객체(mutable)와 변경 불가능한 객체(immutable)이 존재
* 리스트와 딕셔너리는 mutable
* int, string, tuple은 immutable

## default argument
* argument가 여러개인 경우 default 값이 있는 argument는 마지막으로 가야된다.
    * ex) def add_balance(amount: float, name: str = 'checking') -> float:
* argument 당 하나의 default value만 사용가능

## unpack
* [참고자료](https://itholic.github.io/python-pack-unpack-1/)
* 함수 호출 시 argument에 *를 붙어주는 것을 argument unpacking이라 부름
    * add_balance의 parameter가 amount와 name인 경우 add_balance(*t)라 호출 시 amount = t[0], name = t[1]이 argument로 전달된다.
    
## Queue in python
* python에서 양쪽에서 값을 추가하거나 제거할 수 있는 큐를 deque 또는 double ended queue라고 부름


## collections
* counter 
    * 집합에서 각 원소의 출현 횟수를 세어서 원소:출현빈도 식의 dictionary를 생성해 준다.
* defaultdict
    * key error가 절대로 일어나지 않는다.
    * dictionary의 기본값을 정의하고 값이 없을 경우 에러를 출력하지 않고 기본값을 출력하는 기능
* ordereddict
    * dictinary에 삽입한 순서대로 기억
    * python 3.7부터 dictionary 자체에서 삽입한 순서대로 데이터를 기억하기 때문에 유용하지 않다.
* namedtuple 
    * 인덱스를 통해서 접근이 가능한 일반 튜플들과는 달리, 키 값으로 겁근이 가능한 형태
    * class와 비슷해보이지만 custom method를 가지고 있지 않음
    * [참고자료](https://excelsior-cjh.tistory.com/97)
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2010/s10_4.py)

## timezone
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2010/s10_5.py)

## timeit
* [timeit](https://shydev.tistory.com/25)
* 프로젝트의 전체 실행시간이 아닌 특정 함수나 코드의 실행시간을 측정
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2010/s10_6.py)

## Regular expression
* 대표적인 regex
    * `.` : anything - letters, numbers, symbols, ... but not newlines(\n)
    * `+` : one or more of
    * `*` : zero or more of
    * `?` : zero or one of
    
## Regex in Python
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2010/s10_7.py)
* [참고자료](https://wikidocs.net/4308)

## Logging in python
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2010/s10_8.py)
* [참고자료](https://greeksharifa.github.io/%ED%8C%8C%EC%9D%B4%EC%8D%AC/2019/12/13/logging/)