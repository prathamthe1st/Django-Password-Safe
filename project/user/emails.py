from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User


# function to send otp via email
def send_otp(email):
    subject = 'Account login mail'
    otp = random.randint(1000, 9999)
    message = f'Your OTP is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user_obj = User.objects.get(email = email)
    user_obj.otp = otp
    user_obj.save()