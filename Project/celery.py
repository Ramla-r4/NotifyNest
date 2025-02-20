from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

app = Celery('Project')
app.config_from_object('django.conf:settings', namespace='CELERY')

# def add_task():

#     tasks= Tesk.objects.all()
#     for task in tasks :
#         if task.due_date:  # Assuming `due_date` is a DateField in the model
#             schedule_time = {
#                 'day_of_month': task.due_date.day,  # Run on the specific day of the month
#                 'hour': 0,  # Defaults to midnight if not needed
#                 'minute': 0,
#             }
#             app.conf.beat_schedule = {
#                 'send-email-every-monday-morning':{
#                     'task': send_email_task,
#                     'schedule': crontab(**schedule_time),  
#                     # 'args': (task.user_email,),  # Pass additional arguments like email

#                 }
# }
# app.conf.beat_schedule = {
#     'send-due-emails-daily': {
#         'task': 'myapp.tasks.send_due_email_reminder',
#         'schedule': crontab(hour=21, minute=12),  # Run every day at 7:00 AM

#     },
# }

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
