from django.contrib import admin
from .models import UserRegister, Token
# Register your models here.
admin.site.register(UserRegister)
admin.site.register(Token)