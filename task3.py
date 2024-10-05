import re

def normalize_phone(phone_number):
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    if phone_number.startswith('+'):
        return phone_number
    else:
        if phone_number.startswith('380'):
            return '+' + phone_number
        else:
            return '+38' + phone_number



