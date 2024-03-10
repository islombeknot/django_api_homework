import re



def validate_phone_number(phone_number, country_code):
    country_codes = {
        'RU': r'^\+7[0-9]{10}$',          # Rossiya
        'KZ': r'^\+7[0-9]{10}$',          # Qozog'iston
        'KG': r'^\+996[0-9]{9}$',         # Qirg'iziston
        'US': r'^\+1[0-9]{10}$',          # AQSh
        'KR': r'^\+82[0-9]{9,10}$',       # Koreya
        'UZ': r'^\+998[012345789][0-9]{7}$',  # O'zbekiston
    }
    
   
    if country_code in country_codes:
        regex_pattern = country_codes[country_code]
        if re.match(regex_pattern, phone_number):
            return True
    return False


    def clean(self):
        super().clean()
        if self.phone_number:
            country_code = self.phone_number[:2]  
            if not validate_phone_number(self.phone_number, country_code):
                raise ValidationError("Telefon raqami noto'g'ri kiritilgan ")