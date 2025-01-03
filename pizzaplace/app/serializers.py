from rest_framework import serializers
from .models import UserRegister, Token
from django.contrib.auth.hashers import make_password

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserRegister
        fields = ['id', 'name', 'email', 'password']

    def create(self, validated_data):
        # Hash the user's password
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserRegisterSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        # Hash the password if it's being updated
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(UserRegisterSerializer, self).update(instance, validated_data)