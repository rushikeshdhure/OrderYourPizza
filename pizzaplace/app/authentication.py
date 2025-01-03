from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import UserRegister, Token

class TokenAuthentication(BaseAuthentication):
    keyword = 'Token'

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            keyword, key = auth_header.split()
            if keyword != self.keyword:
                return None

            token = Token.objects.get(key=key)
            user = token.user
            return (user, token)
        except (ValueError, Token.DoesNotExist):
            raise exceptions.AuthenticationFailed('Invalid or missing token')