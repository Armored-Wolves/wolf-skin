from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo, User
from .serializers import TodoSerializer, UserSerializer


class UserAPIView(APIView):
    def get(self, request):
        all_users = User.objects.all()
        return Response({'users': UserSerializer(all_users, many=True).data}) #Response converts dict to - JSON

    def post(self, request):
        post_new = User.objects.create(
            username=request.data['username'],
            password=request.data['password']
        )
        return Response('USER Added to DB. And I can alse return a new message from BackEnd')

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #TODO: refactoring !!!
        post_new = Todo.objects.create(
            content=request.data['content'],
            title=request.data['title']
        )
        return Response({'post': TodoSerializer(post_new).data})


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        toDelete = Todo.objects.get(pk=pk)
        toDelete.delete()
        return Response(data=f"Note: {pk} has been removed", status=status.HTTP_204_NO_CONTENT)