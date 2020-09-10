# 섹션 8

* 파이썬은 dynamically typed language로 다른 언어들에 비해 유연
    * 예컨데 Java와 같이 변수 선언 시 타입을 명시해줄 필요가 없다.
* 파이썬에서 함수 선언시 어떤 자료형을 리턴해 줄지 명시가 가능 -> [Type hinting](https://docs.python.org/3/library/typing.html)
    * def add_book(name, author) -> List[Dict(str, Union(str, int)]
    * Type hinting시 None은 아무것도 import할 필요가 없지만 List나 Dict는 from typing import List, Dict가 필요
    * 우리가 새로만든 class를 리턴하는 경우는 아래와 같이한다.
        
      ```python
      from typing import Union, List, Dict  
      Book = Dict(str,Union(str,int))   
      def add_book(name, author) -> List(Book):
          ~~~    
      ```
      
* 함수의 parameter에도 어떤 자료형인지 명시해 줄 수 있다.
    * def add_book(name: str, author: str)
    