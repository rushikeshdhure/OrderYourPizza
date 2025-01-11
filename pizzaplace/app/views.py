from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .serializers import RegisterSerializer,LoginSerializer,PizzaSerializer
from rest_framework.response import Response
from app.models import Register, AddPizza
from django.contrib.auth import login,logout
from rest_framework import status

def index_view(request):
    return render(request, 'index.html')

class RegisterView(APIView):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password')
        }
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
        
        return render(request, self.template_name, {'errors': serializer.errors})


class LoginView(APIView):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('menu')
        return render(request, self.template_name)

    def post(self, request):
        serializer = LoginSerializer(data=request.POST)
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
                        
            # Store user information in session
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            request.session['user_name'] = user.name
            
            # Handle remember me checkbox
            if request.POST.get('checkbox'):
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Until browser closes

            return redirect('menu')  # Replace 'home' with your dashboard URL
        
        # If validation fails, render the template with errors
        return render(request, self.template_name, {'errors': serializer.errors})

class LogoutView(APIView):
    def get(self, request):
        # Clear session
        request.session.flush()
        return redirect('login')
    
class AddPizzaView(APIView):
    def get(self, request):
        try:
            pizzas = AddPizza.objects.filter(is_available=True).order_by('created_at')
            serializer = PizzaSerializer(pizzas, many=True, context={'request': request})
            return Response({
                'status': 'success',
                'message': 'Pizzas fetched successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def ordersview(request):
    return render(request, 'orders.html')


def menu(request):
    return render(request, 'menu.html')