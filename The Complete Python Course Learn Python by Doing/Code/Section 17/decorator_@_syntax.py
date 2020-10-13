user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func


@user_has_permission
def my_function():
    return 'Password for admin panel is 1234.'


@user_has_permission
def another():
    pass
# my_secure_function = user_has_permission(my_function)


print(my_function.__name__)
print(another.__name__)
