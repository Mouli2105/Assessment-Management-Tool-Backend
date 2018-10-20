from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')