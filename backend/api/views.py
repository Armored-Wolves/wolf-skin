from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo, User
from .serializers import TodoSerializer, UserSerializer


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def post(self, request):
        post_new = Todo.objects.create(
            content=request.data['content'],
            title=request.data['title']
        )
        return Response('Notes Added TO DB')

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserAPIView(APIView):
    def get(self, request):
        all_users = User.objects.all().values()
        return Response({'users': list(all_users)}) #Response converts dcit to - JSON

    def post(self, request):
        post_new = User.objects.create(
            username=request.data['username'],
            password=request.data['password']
        )
        return Response('USER Added to DB. And I can alse return a new message from BackEnd')

    #TODO: Test