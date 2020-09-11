def starts_with_r(friend):
    return friend.startswith('R')


friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(starts_with_r, friends)
"""
위에 함수를 선언하지 않고 lamba 이용해도 가능
start_with_r = filter(lambda friend: friend.startswith('R'), friends)
"""

another_starts_with_r = (f for f in friends if f.startswith('R'))  # start_with_r과 같음 generator comprehension 사용
print(list(start_with_r))
print(list(start_with_r))  # empty list가 return 됨. start_with_r은 generator로 위에서 이미 end에 도달했기 때문이다.
print(list(another_starts_with_r))


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


my_start_with_r = my_custom_filter(starts_with_r, friends)
print(list(my_start_with_r))