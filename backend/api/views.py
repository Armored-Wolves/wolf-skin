from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo, User
from .serializers import TodoSerializer, UserSerializer


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        post_new = User.objects.create(
            username=request.data['username'],
            password=request.data['password']
        )
        print(post_new)
        return Response(200)

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