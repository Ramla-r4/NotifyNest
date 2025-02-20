# # tasks.py
from celery import shared_task
from django.core.mail import send_mail


from .models import Tesk
@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(subject, message, 'notifynest0@gmail.com',recipient_list,fail_silently=False), 

# def send_due_email_reminder():
#     # Get all tasks due today
#     tasks = Tesk.objects.filter(due_date=date.today())
    
#     for task in tasks:
#         subject = 'Task Due Reminder'
#         message = f"Reminder: {task.task_name} is due!"
#         recipient_list = [task.user_email]
#         send_mail(subject, message, 'notifynest0@gmail.com', recipient_list)

# from celery import shared_task
# # from django.core.mail import send_mail
# from django.http import HttpResponse
# # from .models import Tesk  # Adjust the import based on your model's location
# from datetime import date
# @shared_task
# def add():
#     for i in range(11):
#         print(i)
