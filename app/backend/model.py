from flask_login import UserMixin
from app.backend.db import *


class User(UserMixin):

    def __init__(self, id: int, name: str, email: str, phone:str, image: str):

        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.image = image
