# 섹션 11

* [강의제공 자료](https://github.com/tecladocode/complete-python-course/tree/master/course_contents/11_web_scraping/projects)

## Scarping
* 페이지 다운로드부터 데이터 추출까지 모든 작업

## BeautifulSoup
* from bs4 import BeautifulSoup가 필요
* BeautifulSoup({파싱하려는 HTML},{어떤 유형의 문서인지}) ex) BeautifulSoup(SIMPLE_HTML, 'html.parser')
* find()`
    * 해당 조건에 맞는 태그를 가져온다.
    * 두 번째 argument는 가져오려는 속성 값을 명시할 수 있다. ex) bs.find('div',{'class': 'shin'})
* find_all()
    * 해당 조건에 맞는 모든 태그를 가져온다.
    
## requests
* import requests가 필요
* Python에서 HTTP 요청을 보내는 라이브러리

## log 남기기

```python
import logging


logging.basicCongig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] $(messages)s',
                    datefmt='%d-%m-%Y %H%:%M:%S',
                    level= logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Lodaing book list...')
```


