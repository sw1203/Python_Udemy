from datetime import datetime, timezone, timedelta

print(datetime.now())  # 현재 operating system의 시간을 반환해줌

print(datetime.now(timezone.utc))  # universal time standard의 시간을 반환해줌

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)  # 오늘 날짜를 기준으로 24시간 후
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M'))  # 출력 양식을 설정할 수 있음

user_date = input('Enter the date in YYYY-mm--dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # 우리가 설정한 양식대로 시간을 문장을 시간으로 parsing해줌

print(user_date)