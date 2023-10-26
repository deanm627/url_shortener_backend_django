from rest_framework import serializers
from .models import URL

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['title', 'long_url', 'short_url', 'user']

    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # token["custom_field"] = "Custom value"

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        data["user_id"] = user.id
        data["first_name"] = user.first_name
        # data["username"] = user.username
        # ... add other user information as needed

        return data
