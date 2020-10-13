# iterable argument를 받겠다는 의미
def add_all(*args):
    return sum(args)


print(add_all(5, 7, 3, 4))


def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')


pretty_print(**{'username': 'jose123', 'access_level': 'admin'})
