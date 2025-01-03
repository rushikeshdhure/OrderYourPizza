from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserRegister, Token
from .serializers import UserRegisterSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .authentication import TokenAuthentication
# Create your views here.
from django.shortcuts import render,redirect
def index_view(request):
    return render(request, 'index.html')

# def login(request):
#     return render(request, 'login.html')

# def register(request):
#     return render(request, 'register.html')
class RegisterView(APIView):
    def get(self, request):
        serializer = UserRegisterSerializer()
        return render(request, 'register.html', {'serializer': serializer})

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')  # Replace with your desired redirect
        else:
            return render(request, 'register.html', {'serializer': serializer})

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = UserRegister.objects.get(email=email)
            if check_password(password, user.password):
                # Create or retrieve the token for the user
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)
        except UserRegister.DoesNotExist:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'You have been logged out.'}, status=status.HTTP_200_OK)

class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': f'Hello, {request.user.name}!'}, status=status.HTTP_200_OK)