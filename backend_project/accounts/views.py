# from .models import CustomUser
# from rest_framework.views import APIView
# from .serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# # Create your views here.
# class LoginView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.data["username"]
#         print(user)
#         queryset = CustomUser.objects.filter(username=user)
#         print(queryset)
#         # serializer_class = UserSerializer
#         return Response(queryset)