from rest_framework import serializers
from .models import User



# serializer to serialize api input/output
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified']


# serializer to verify otp input/output
class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()