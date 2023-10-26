from .models import URL
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import URLSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class UserURLView(APIView):
    def get(self, request):
        print('helloooo')
        print(request.query_params)
        param = request.query_params
        data = dict(param)
        print(data)
        user_id = data.get('user')
        print(user_id[0])
        queryset = URL.objects.filter(user=user_id[0])
        print(queryset)
        serializer = URLSerializer(queryset, many=True)
        return Response(serializer.data)

class URLViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = URL.objects.all()
    serializer_class = URLSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
        serializer_class = CustomTokenObtainPairSerializer