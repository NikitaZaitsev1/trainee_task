from enum import Enum


class Role(str, Enum):
    admin = 'admin'
    moderator = 'moderator'

class HttpMethod(str, Enum):
    get = 'get'
    retrieve = 'retrieve'
    update = 'update'
    delete = 'delete'

