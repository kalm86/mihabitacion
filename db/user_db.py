from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    balance: int

database_users = Dict[str, UserInDB]
database_users = {
    "kalm": UserInDB(**{"username":"kalm86",
                        "password":"12345"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None