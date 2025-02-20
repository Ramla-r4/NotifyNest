from.models import Tesk
from django import forms
from django.utils.timezone import now



# class (forms.ModelForm):
#     Name_tesk = forms.CharField(required=True,widget=forms.TextInput(attrs={ 'class':'form-control'}),label=' Name Of Tesk')
#     Detial_tesk =  forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control'}),label='Detial Of Tesk')
#     # Reminder_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'form-control'}), label='Due Date')
#     User_email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Email , It's Optinal If you Want To Get Reminder")
   
  

class OrginazeTesk(forms.ModelForm):
    task_name = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control'}),label='Tesk Name ')
    task_description = forms.CharField(widget=forms.Textarea(attrs={ 'class':'form-control'}),label='Detial Of Tesk')
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'form-control'}), label='Due Date')
    user_email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),label="User Email,It's Optinal ,If you Want To Get Reminder") 
    class Meta:
        model = Tesk
        exclude = ("user",)

