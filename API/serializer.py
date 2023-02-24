from rest_framework import serializers
from core. models import *

class UserSerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length = 8, default=Types.CLIENTS)
    class Meta:
        model = client
        fields = ["email", "is_verified", 'type']

class verifyaccount(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
