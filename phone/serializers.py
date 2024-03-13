from rest_framework import serializers
from .models import User, UserCodeVarivication, CountryCode,RU, KZ, KG, US, KR, UZ
from .utils import send_sms
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import ValidationError
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'auth_code', 'phone_number']
        

    def validate_phone_number(self, value):
        return value
    def create(self, validated_data):
            user = super(UserSerializer,self).create(validated_data)
            country_code = validated_data.get('auth_type')

            if country_code == RU :
               code = user.create_confirmation_code(RU)
               send_sms(code)

            elif country_code == KZ:
               code = user.create_confirmation_code(KZ)
               send_sms(code)  
            elif country_code == KG:
               code = user.create_confirmation_code(KG)
               send_sms(code)
            elif country_code == US:
               code = user.create_confirmation_code(US)
               send_sms(code) 
            elif country_code == KR:
               code = user.create_confirmation_code(US)
               send_sms(code) 
            elif country_code == UZ:
               code = user.create_confirmation_code(UZ)
               send_sms(code)
            else:
               data = {
                        "status":False,
                        "message":"kode yuborishda xatolik boldi"
                 }
               raise ValidationError(data)
                  

    def to_representation(self, instance):
        data = super(UserSerializer,self).to_representation(instance)
        
        data['access'] = instance.token()['access']
        data['refresh'] = instance.token()['refresh']
     
        return data
     