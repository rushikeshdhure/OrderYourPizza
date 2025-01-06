from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response

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
            return redirect('login.html')
        
        return render(request, self.template_name, {'errors': serializer.errors})
    

