# serializers.py
from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['name', 'email', 'password']