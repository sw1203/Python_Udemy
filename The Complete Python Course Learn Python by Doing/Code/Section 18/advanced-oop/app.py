from admin import Admin
from database import Database
from user import User

a = Admin('rolf', '1234', 3)
u = User('jose', 'password')

a.save()

users = [a, u]
for user in users:
    user.save()
