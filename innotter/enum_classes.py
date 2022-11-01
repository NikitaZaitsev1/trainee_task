from enum import Enum


class Role(str, Enum):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'


class Method(str, Enum):
    GET = 'GET'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    LIST = 'list'
    CREATE = 'create'
    RETRIEVE = 'retrieve'
    UPDATE = 'update'
    PARTIAL_UPDATE = 'partial_update'
