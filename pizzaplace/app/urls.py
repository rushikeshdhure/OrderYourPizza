from django.urls import path
from .views import index_view, RegisterView,LoginView

urlpatterns = [
    path('', index_view, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

]