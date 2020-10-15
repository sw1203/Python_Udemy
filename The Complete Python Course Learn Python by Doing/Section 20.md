# 섹션 20

- [강의 제공 코드](https://www.udemy.com/course/the-complete-python-course/learn/lecture/15227268#overview)
- [unittest documentation](https://docs.python.org/ko/3/library/unittest.html)
- [참고자료](https://www.daleseo.com/python-unittest-testcase/)

## unit testing
- 목적
    - 프로그램이 무엇을 수행하는지 그리고 프로그램에서 함수가 어떤 역할을 하는지
    - 프로그램이 변경 될때 잘 실행되는 지
- import unittest가 필요

## Testing functions
- self.assertEqual(A, B) -> A와 B가 같은 값을 가지는지 확인
- self.assertAlmostEqual(A, B, delta=0.0001) -> A와 B의 차이가 0.0001이하면 test 통과
- [functions 실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2020/functions.py)
- [test_functions 실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2020/test_functions.py)

## Testing class
- [Printer Class 실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2020/printer.py)
- [test_printer 실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2020/test_print.py)
