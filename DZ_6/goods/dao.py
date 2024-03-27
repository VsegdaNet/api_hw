from dao import BaseDAO
from user.models import User 

class UserDAO(BaseDAO):
    model = User