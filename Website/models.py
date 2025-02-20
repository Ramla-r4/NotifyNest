from django.db import models
from django.contrib.auth.models import User

class Tesk(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE)
   task_name =  models.CharField(max_length= 100)
   task_description = models.TextField()
   due_date = models.DateTimeField()
   user_email = models.EmailField(default='', blank=False)

   def __str__(self):
        return self.task_name 