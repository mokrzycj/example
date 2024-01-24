# utils.py w aplikacji notifications

from django.core.mail import send_mail

def send_notification_email(subject, message, recipient_list):
    send_mail(subject, message, 'from@example.com', recipient_list)
