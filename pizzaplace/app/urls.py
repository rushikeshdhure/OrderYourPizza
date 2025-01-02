from django.urls import path
from .views import index_view, login

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login, name='login'),
    # comment
]