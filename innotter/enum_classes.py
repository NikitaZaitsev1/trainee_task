from enum import Enum


class Role(str, Enum):
    admin = 'admin'
    moderator = 'moderator'


class Method(str, Enum):
    get = 'GET'
    retrieve = 'retrieve'
    update = 'UPDATE'
    delete = 'DELETE'
