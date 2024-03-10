from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'auth_code', 'phone_number']
        

    def validate_phone_number(self, value):
        return value
