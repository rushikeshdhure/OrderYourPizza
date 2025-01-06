# serializers.py
from rest_framework import serializers
from .models import Register

from django.core.exceptions import ValidationError
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['name', 'email', 'password']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = Register.objects.get(email=email, password=password)
                data['user'] = user
            except Register.DoesNotExist:
                raise ValidationError('Invalid email or password.')
        else:
            raise ValidationError('Must provide email and password.')
        
        return data