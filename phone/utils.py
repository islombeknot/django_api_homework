import re
from rest_framework.validators import ValidationError
from .models import User
import threading 
import requests 


def validate_phone_number(phone_number, country_code):
    country_codes = {
        'RU': r'^\+7[0-9]{10}',          # Rossiya
        'KZ': r'^\+7[0-9]{10}',          # Qozog'iston
        'KG': r'^\+996[0-9]{9}',         # Qirg'iziston
        'US': r'^\+1[0-9]{10}',          # AQSh
        'KR': r'^\+82[0-9]{9,10}',       # Koreya
        'UZ': r'^\+998[012345789][0-9]{7}',  # O'zbekiston
    }
   
    if country_code in country_codes:
        regex_pattern = country_codes[country_code]
        if re.match(regex_pattern, phone_number):
            return True
        return False



class SmsThread(threading.Thread):

     def __init__(self, sms):
          self.sms = sms
          super(SmsThread, self).__init__()

     def run(self):
          send_message(self.sms)

def send_message(message_text):
     url = f'https://core.telegram.org/bots/api6735012647:AAHympVvmYnETcsa0Heo-_Iqlz2NZ1JcXKE/sendMassage'
     params = {
          'chat_id':"",
          'text':message_text,
     }

     response = requests.post(url, data=params)
     return response.json()

def send_sms(sms_text):
     sms_thread = SmsThread(sms_text)

     sms_thread.start()

     sms_thread.join()

