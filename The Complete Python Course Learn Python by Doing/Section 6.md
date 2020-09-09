# 섹션 6

* [강의제공 자료](https://github.com/tecladocode/complete-python-course/tree/master/course_contents/6_files)

## Files in python

* open('파일명', '읽기(r), 쓰기(w), 이어쓰기(a)') 
* 'w'는 기존 파일내용을 다 지우고 새로운 내용을 작성한다.
* .read()는 파일의 전체 내용을 읽음
* .readlines()는 파일의 내용을 라인별로 읽어서 리스트 형태로 나타내준다. 
    * ex) [line1, line2, ...]
    * 파일에서 line을 읽을 때 line끝에 '\n'이 존재 -> .strip() 사용시 없앨 수 있음
* open했던 파일을 닫는 역할
* 파일을 읽고 close하는 것은 굉장히 중요하다. close하지 않으면 문제를 야기할 수 있다.
* 사용자에 입력받은 것을 파일로 쓰려할 때 입력을 먼저 받고 파일을 open하는 것이 좋다.
* .write()는 파일에 string을 쓰는 역할

## Python Exercise : copying files

* [강의 실습 코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%206/friends.py)

## CSV files in python

* [강의 실습 코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%206/csv_read.py)
* CSV module(내장 모듈)을 이용하면 편하다
* .csv 파일을 읽기 모드로 오픈하고 파일객체를 csv.reader(파일객체)에 넣으면 된다.
* .csv 파일을 쓰기 모드로 오픈하고 파일객체를 csv.writer(파일객체)에 넣으면 된다.
* CSV writer는 writerow()라는 메서드를 데이터를 추가
* [참고자료](http://pythonstudy.xyz/python/article/207-CSV-%ED%8C%8C%EC%9D%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
* [강의 제공 참고자료](https://www.youtube.com/watch?v=W7QByFjVom8)

## JSON files with python

* [강의 실습 코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%206/json_imports.py)
* [강의 실습 코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%206/a%20csv%20to%20json%20converter.py)
* JSON과 Python dictionary 차이점
    * JSON은 문자열이다. Text file이기 때문
    * JSON은 ""를 이용한다. ''는 사용하지 않는다.
* JSON module(내장 모듈)을 이용한다.
    * JSON module은 object나 class가 아니다.
* json.load({파일포인터}) : 파일안의 내용을 읽어서 딕셔너리로 반환한다.
* json.dump({object}, {파일포인터}) : object를 json 형식으로 변환시켜 파일에 쓸 수 있다.
* json.loads({string}) : load와 다르게 첫번째 argument가 string이다. 
* dicitionary, list는 json으로 변환이 가능하지만 tuple은 불가능하다.

## 'with' statement

* [context manager](https://suhwan.dev/2017/12/29/Python3-Context-Manager/) 의 일종
* with {function} as {variable}: function의 반환 값이 variable에 할당됨.
* 아래 코드와 같이 open을 with와 사용하면 indented block이 종료되고 나서 자동으로 파일이 close된다.

```python
with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)
``` 

## importing our own files

* [강의 실습 코드](https://github.com/sw1203/Python_Udemy/tree/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%206/imports_project)
* importing은 다른 파일에 정의된 코드를 현재 작업중인 파일에서 사용할 수 있도록 하는 것
* directory 안에 __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할
* import 시에 import한 파일이 먼저 실행되고 현재 작업중인 파일이 실행된다.