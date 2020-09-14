class User:
    def __init__(self, username, password):
        self.username = username,
        self.password = password


# imagine these users are coming from a database...
users = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}
]

user_objects = [User(**data) for data in users]  # user_objects = [User(username=data['username'], password=data['password']) for data in users] 같은 의미이다.
