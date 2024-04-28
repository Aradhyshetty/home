from django.core.mail import send_mail
import uuid
from django.conf import settings



def send_forget_password_mail(email):
    subject="your password reset link"
    message =f"hi,click here to change   by team Logway"
    email_from =settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list,fail_silently=False)
    return True