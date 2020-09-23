# 섹션 12

* [강의제공 자료](https://github.com/tecladocode/complete-python-course/tree/master/course_contents/12_browser_automation_selenium)
* [참고자료 1](https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html)
* [참고자료 2](https://sacko.tistory.com/13)

## webdriver
* 프로그래밍 언어를 이용해서 브라우저를 자동화할 수 있게 해줌
* from selenium import webdriver 필요

## Selenium Explicit waits
* Selenium Webdriver를 이용해서 크롤링을 진행 시 JS처리가 끝나지 않은 상태에서 JS로 그려지는 HTML 엘리먼트를 가져오려고 하는 경우가 발생할 수 있음
* 브라우저가 HTML Elemenet를 기다리도록 만드는 방법 중 하나
* 명확하게 특정 element가 나타날 때까지 기다려주는 방식
* 아래 3가지가 필요

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
```

## Selenium Implicit waits
* 지정한 시간동안 기다림
* driver.implicitly_wait(3) : 3초를 기다리겠다는 의미
* 지정한 시간만큼 무조건 기다려야 되기 때문에 추천하지 않음

