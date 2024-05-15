from django.urls import path
from .views import ListTodo, DetailTodo
from .views import UserAPIView

urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('notes/', ListTodo.as_view()),
    path('notes/<int:pk>', DetailTodo.as_view()),
]