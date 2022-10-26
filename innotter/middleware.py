import json
import logging
import os

import jwt

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class MiddlewareAuthenticationJWT(MiddlewareMixin):

    def process_request(self, request):
        if jwt_token := request.headers.GET('authorization'):
            try:
                payload = jwt.decode(jwt_token, os.getenv('JWT_SECRET_KEY'), algorithms=[os.getenv('JWT_ALGORITHMS')])
                useruuid = payload['user_uuid']
                logger.info(f"Request received from user - {useruuid}")
            except jwt.ExpiredSignatureError:
                msg = "Authentication token has expired"
                logger.info(f"Response: {msg}")
                return HttpResponse(json.dumps({"message": msg}), status=401)
            except (jwt.DecodeError, jwt.InvalidTokenError):
                msg = "Authorization has failed, Please send valid token."
                logger.info(f"Response: {msg}")
                return HttpResponse(json.dumps({"message": msg}), status=401)
        else:
            msg = "Authorization not found, Please send valid token in headers"
            logger.info(f"Response: {msg}")
            return HttpResponse(json.dumps({"message": msg}), status=401)
