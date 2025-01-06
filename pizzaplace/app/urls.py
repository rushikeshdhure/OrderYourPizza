from django.urls import path
from .views import index_view, RegisterView

urlpatterns = [
    path('', index_view, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', name='login')

]