from .models import CustomUser
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .forms import CustomUserCreationForm, NewUserForm

# Create your views here.
class RegisterView(APIView):
    
    def post(self, request):
        # print(request.data['password'])
        # print(make_password(request.data['password']))
        # user_info = request.data
        # hash_password = make_password(request.data['password'])
        # user_info['password'] = hash_password
        # print(user_info)
        
        form = NewUserForm(request.data)
        print(form)
        if form.is_valid():
            user = form.save()
            user.password = make_password(request.data['password'])
            user.save()
        return Response("is this working?")

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.data["username"]
        print(user)
        queryset = CustomUser.objects.filter(username=user)
        print(queryset)
        # serializer_class = UserSerializer
        return Response(queryset)