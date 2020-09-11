# 섹션 9
* [실습코드](https://github.com/sw1203/Python_Udemy/tree/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%209)

## Generators
* [참고자료](https://bluese05.tistory.com/56)
* 함수가 실행되는 도중의 상태들을 기억하는 함수로 함수가 여러번 실행 될때 그 직전의 결과를 기억하는 함수
* 한 번에 모든 값이 필요한 것이 아니라 one by one이 필요한 경우 유용
    * 예컨데 1을 가지고 어떠한 것을 수행하고 난 다음에 2가 필요한 경우
* list 전체를 메모리에 기억하는 것이 아니라 마지막 사용한 element를 기억하고 있다가 다음 element를 사용하게 해줌
* yield는 return과 비슷하지만 우리가 호출하는 경우에만 return하고 함수는 yield의 라인에서 정지
    * 아래 예시에서는 4번째 줄과 5번째 줄 사이에서 정지
    * 이후 generator 함수 다시 호출시 5번째 줄부터 다시 시작해서 또 4번째 줄과 5번째 줄 사이에서 정지
* next()는 generator에 영향을 미치는 내장 함수로, yeild의 값을 받아오기 위해 사용


```python
def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


g = hundred_numbers()
print(next(g))
print(next(g))
print(list(g))
```    

## generator class

```python
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


my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))
```

## Iterables
* Iterable은 __iter__() method를 가지고 있는 object
* __len()__과 __getitem()__ method를 가지고 있어도 Iterable

## Iterator vs Iterable
* [참고자료](https://wikidocs.net/16068)
* Iterator : 다음 value를 얻는데 사용
* Iterable : Iterator의 모든 value를 탐색하는데 사용

## filter()
* [참고자료](https://wikidocs.net/22803) - map설명도 같이 있음
* 첫번째 argument는 Ture/False를 반환하는 function
* 두번째 argument는 iterable
* filter는 generator를 return

## map()
* map 함수는 iterable을 받고 새로운 iterable을 반환한다

## False values
* 0, 0.0
* None
* [], (), {}
* False

## any() and all()
* any 함수는 각 element를 살펴보며 bool()을 통해 참인지 거짓인지를 보고 하나라도 참이면 참을 반환한다.
* all 함수는 any와 달리 하나라도 거짓이 존재하면 거짓을 반환
 