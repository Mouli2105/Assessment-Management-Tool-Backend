from rest_framework.serializers import ModelSerializer
from Tool.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')