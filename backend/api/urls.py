from django.urls import path
from .views import ListTodo, DetailTodo
from .views import UserAPIView

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('user/', UserAPIView.as_view()),
]