from django.urls import path
from .views import index_view, login,register

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]