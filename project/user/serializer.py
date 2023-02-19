from rest_framework import serializers
from .models import User



# serializer to serialize api input/output
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified']