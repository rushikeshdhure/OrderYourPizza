# serializers.py
from rest_framework import serializers
from .models import Register,AddPizza
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

                if user:
                    if user.is_active:
                        data['user'] = user
                    else:
                        raise serializers.ValidationError('User account is disabled.')
                else:
                    raise serializers.ValidationError('Invalid email or password.')
            except Register.DoesNotExist:
                raise serializers.ValidationError('Invalid email or password.')
        else:
            raise serializers.ValidationError('Must provide email and password.')
        
        return data
    

class PizzaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = AddPizza
        fields = ['id', 'name', 'description', 'price', 'image', 'is_available', 'created_at']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None