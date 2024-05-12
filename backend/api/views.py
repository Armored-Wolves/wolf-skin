from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo, User
from .serializers import TodoSerializer


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserAPIView(APIView):
    def get(self, request):
        all_users = User.objects.all().values()
        print(all_users)
        return Response({'users': list(all_users)}) #Response converts dcit to - JSON

    def post(self, request):
        return Response({'title': 'POST requests dont work'})