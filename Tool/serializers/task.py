from rest_framework.serializers import ModelSerializer
from Tool.models import *

class TaskSerializer(ModelSerializer):
    class Meta:
        model  = Task
        fields = '__all__'