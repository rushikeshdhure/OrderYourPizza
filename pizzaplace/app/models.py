from django.db import models
from django.contrib.auth.hashers import make_password
import binascii
import os
class UserRegister(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def save(self, *args, **kwargs):
        # Hash the password before saving the user object
        if not self.pk or 'password' in kwargs.get('update_fields', []):
            self.password = make_password(self.password)
        super(UserRegister, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    @property
    def is_authenticated(self):
        return True  # Required for DRF authentication

    @property
    def is_anonymous(self):
        return False  # Required for DRF authentication
    


class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(UserRegister, related_name='auth_token', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            # Generate a unique authentication key
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key