# random_mail.py
import random
import string

def email_here():
    rand_mail = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    full_mail = f"{rand_mail}@mailinator.com"
    print(f"Generated email: {full_mail}")
    return full_mail
