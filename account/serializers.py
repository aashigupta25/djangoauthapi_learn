
from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerilizer):
    password2 = serializers.CharField(style = {'input_type':'password'}, write_only = True)
    class Meta:
        Model = User
        Field = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs= {
            'password' : {'write_only': True}
        }