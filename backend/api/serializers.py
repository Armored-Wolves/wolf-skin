from rest_framework import serializers
from .models import Todo, User


class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    class Meta:
        model = Todo
        fields = '__all__'



class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=20)
    class Meta:
        model = User
        fields = '__all__'