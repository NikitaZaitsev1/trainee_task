from enum import Enum


class Role(str, Enum):
    admin = 'admin'
    moderator = 'moderator'


class Method(str, Enum):
    GET = 'GET'
    RETRIEVE = 'retrieve'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
