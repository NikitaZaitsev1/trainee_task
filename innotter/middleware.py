import json
import os

import jwt

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


def create_response(message):
    try:
        data = {"data": message}
        return data
    except Exception as creation_error:
        print(f'create_response:{creation_error}')


class MiddlewareAuthenticationJWT(MiddlewareMixin):

    def process_request(self, request):

        jwt_token = request.headers.get('authorization', None)
        print(f"request received for endpoint {str(request.path)}")

        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, os.getenv("JWT_SECRET_KEY"), algorithms=['HS256'])
                useruuid = payload['user_uuid']
                print(f"Request received from user - {useruuid}")
                return None
            except jwt.ExpiredSignatureError:
                response = create_response({"message": "Authentication token has expired"})
                print(f"Response {response}")
                return HttpResponse(json.dumps(response), status=401)
            except (jwt.DecodeError, jwt.InvalidTokenError):
                response = create_response({"message": "Authorization has failed, Please send valid token."})
                print(f"Response {response}")
                return HttpResponse(json.dumps(response), status=401)
        else:
            response = create_response({"message": "Authorization not found, Please send valid token in headers"}
                                       )
            print(f"Response {response}")
            return HttpResponse(json.dumps(response), status=401)
