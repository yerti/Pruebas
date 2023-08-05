#!/usr/bin/python3
"""create una class user"""

from models.base_model import BaseModel

class user(BaseModel):

    def __init__(self, *arg, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""


