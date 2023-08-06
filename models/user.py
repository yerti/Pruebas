#!/usr/bin/python3
"""create una class user"""

from models.base_model import BaseModel

class User(BaseModel):

        email = ""
        password = ""
        first_name = ""
        last_name = ""


