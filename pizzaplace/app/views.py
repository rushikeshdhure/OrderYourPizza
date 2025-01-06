from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response

def index_view(request):
    return render(request, 'index.html')

# def register_view(request):
#     return render(request, 'register.html')

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response({
#             'message' : 'User registered successfully',
#             'register' : serializer.data
#         })

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