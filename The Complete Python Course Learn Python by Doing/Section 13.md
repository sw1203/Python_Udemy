# 섹션 13
* [강의제공 자료](https://github.com/tecladocode/complete-python-course/tree/master/course_contents/13_async_development/sample_code)

## 용어 정리
* Synchronous : 차례로 발생하는 작업으로 각 라인은 이전 라인 이후에 실행
* Asynchronous : 작업이 순서대로 실행되는 것이 아니라 임의의 순서로 실행

## Python GIL (Global Interpreter Lock)
* [참고자료](https://dgkim5360.tistory.com/entry/understanding-the-global-interpreter-lock-of-cpython)
* 프로세스가 생성하고 스레드를 획득해야 하는 리소스
* 두개의 쓰레드를 동시에 실행시키지 못함
* OS에서 쓰레드에 우선순위를 부여하여 쓰레드를 대기시켜줌

## thread
* import threading이 필요
* .join()은 메인쓰레드가 다른 쓰레드들이 종료될때까지 대기하게 만드는 것
* CPU 할당 시간을 나눠서 실행함으로써 겉으로 보기에 두개가 동시에 실행되는 것 처럼 보이게 만든다.
* 명령들이 순차적으로 실행되어야 하는 경우에는 thread를 이용하지 않는 것이 좋다. 만약 쓰레드를 이용하고 싶으면 queuing system으로 만들어라
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2013/threads.py)

## concurrent.futures
* Threadpoolexecutor는 대상이 없는 쓰레드 묶음(쓰레드 풀)을 생성하고 해당 풀을 사용하여 작업 또는 함수를 실행할 수 있게 해준다.
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2013/concuurent_futures.py)

## multiprocessing in Python
* import multiporcessing이 필요
* user input을 받는 것 처럼 waiting이 필요하지 않고 두가지 일을 동시에 실행시켜야한다면 multi processing을 사용
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2013/processes.py)

## Queuing in threads with shared state
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2013/queued_threads.py)

## generator
* [실습코드1](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2013/generators.py)
* [실습코드2](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2013/receiving_through_yield.py)
* [실습코드3](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2013/yielding_two_way.py)

## async and await
* [coroutine](https://dojang.io/mod/page/view.php?id=2418)
* [asyncio](https://kdw9502.tistory.com/6)
* [실습코드](https://github.com/sw1203/Python_Udemy/blob/master/The%20Complete%20Python%20Course%20Learn%20Python%20by%20Doing/Code/Section%2013/async_await.py)

