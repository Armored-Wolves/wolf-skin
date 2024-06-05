from django.urls import path
from .views import ListTodo, DetailTodo, UserView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('notes/', ListTodo.as_view()),
    path('notes/<int:pk>', DetailTodo.as_view()),
]