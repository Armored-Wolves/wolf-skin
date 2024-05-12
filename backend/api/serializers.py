from rest_framework import serializers
from .models import Todo, User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'