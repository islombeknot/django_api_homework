from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import uuid
from .utils import validate_phone_number
from django.db import models
from rest_framework.validators import ValidationError
 
# Create your models here.
class BaseModel(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
          abstract = True
# COUNTRY CODES 
RU = 'RU'
KZ = 'KZ'
KG = 'KG'
US = 'US'
KR = 'KR'
UZ = 'UZ'


# REGISTER COUNTRY CODES
COUNTRY_CODES = {
     RU: 'Россия',
     KZ: 'Казахстан',
     KG: 'Киргизия',
     US: 'Америка',
     KR: 'Корея',
     UZ: 'Узбекистан',
}

# VIA CODE 
VIA_RU = '+7'
VIA_KZ = '+7'
VIA_KG = '+996'
VIA_US = '+1'
VIA_KR = '+82'
VIA_UZ = '+998'


class User(AbstractUser):
    AUTH_CODES = (
        ('RU', 'Russia'),
        ('KZ', 'Kazakhstan'),
        ('KG', 'Kyrgyzstan'),
        ('US', 'United States'),
        ('KR', 'South Korea'),
        ('UZ', 'Uzbekistan'),
    )

    auth_code = models.CharField(max_length=2, choices=AUTH_CODES)
    phone_number = models.CharField(max_length=17, unique=True, blank=True, null=True)
    def clean(self):
        super().clean()
        if self.phone_number:
           
            if not validate_phone_number(self.phone_number, self.auth_code):
                raise ValidationError("Telefon raqami noto'g'ri formatda")
    @property

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
     
def check_username(self):
     temp_username = self.username  # Initialize with current username
     if not temp_username:
        temp_username = f"telegram-{str(uuid.uuid4()).split('-')[-1]}"

     while User.objects.filter(username=temp_username).exists():
        temp_username = f"{temp_username}{random.randint(0, 9)}"

     self.username = temp_username


     def check_pass(self):
          if not self.password:
               temp_password = f"telegram-{str(uuid.uuid4()).split('-')[-1]}"
               self.password = temp_password
          
     def check_hash_password(self):
          if not self.password.startswith('pbkdf2_'):
               self.set_password(self.password)
     
     
     def save(self, *args, **kwargs):
          self.check_username()
          self.check_pass()
          self.check_hash_password()


          super(User,self).save(*args, **kwargs)
class UserCodeVarivication(BaseModel):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_code_varivication')
     def create_confirmation_code(self,auth_type):
          code = "".join([str(random.randint(0, 9)) for _ in range(4)])

          UserCodeVarivication.objects.create(
               code=code,
               auth_type=auth_type,
               user_id=self.id

          )
          return code

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

     
    


