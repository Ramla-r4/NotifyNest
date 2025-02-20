from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from.models import Tesk
from .forms import OrginazeTesk
from django.shortcuts import render
from django.shortcuts import render
# from django.utils.timezone import make_aware
# from datetime import datetime, timezone
from .models import Tesk
from.tasks import send_email_task
# from django_celery_beat.models import PeriodicTask,ClockedSchedule
@login_required
def home(request):
    tasks = Tesk.objects.filter(user=request.user)
    return render(request, 'Pages/home.html', {'tasks':tasks,'user': request.user},)

def index(request):
    tasks = Tesk.objects.all()
    for task in tasks:
            if task.due_date >= now():
					
               subject = 'Welcome to Our Website'
               message = f"Reminder: {task.task_name} is due!"
               recipient_list = [task.user_email]
               send_email_task.delay(subject, message, recipient_list)
    return render(request, 'Pages/index.html')


def login_user(request):
	# if request.method == 'POST':
	# 	username = request.POST['username']
	# 	password = request.POST['password']
	# 	if User.objects.filter(username=username).exists():
	# 		messages.info(request, 'Username Is Already Taken. Please Choose Another One.')
	# 		return redirect('login')
	# 	else:
	# 		user1 =User.objects.create_user(username=username,password=password)
	# 		user1.save()
	# 		messages.info(request, 'You Have Been Logged')
	# 		return redirect('home')
	# else:
	#   return render(request, 'All/login.html')

    if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect("/admin/")
                messages.success(request, 'You have been logged in!')
                return redirect('home')  # Redirect to home page
            else:
                messages.info(request, 'Invalid credentials. Please try again.')
                return redirect('registration/login.html')  # Redirect back to login page
    elif 'signup' in request.POST:  # Check if the signup button was clicked
            username = request.POST['username']
            password = request.POST['password']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken. Please choose another one.')
                return redirect('login')  # Redirect back to login page
            else:
                user = User.objects.create_user(username=username, password=password)
                user.is_superuser = False
                user.is_staff  =False
                user.save()
                messages.success(request, 'Your account has been created! Please log in.')
                return redirect('login')  # Redirect to login page after signup
    return render(request, 'registration/login.html')  # Render the login/signup page

            


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('index')



@login_required
def add_tesk(request):
    if request.method == "POST":
        form = OrginazeTesk(request.POST)  # Bind form to POST data
        if form.is_valid():
            add_tesk = form.save(commit=False)  # Don't save to DB yet
            add_tesk.user = request.user  # Attach the user to the task
            add_tesk.save()  # Now save the task to the database
            messages.success(request, "Task Added Successfully.")
            return redirect('home')  # Redirect to home or another view after success
    else:
        form = OrginazeTesk()  # Show an empty form if it's a GET request
    
    return render(request, 'Pages/add_tesk.html', {'form': form})

		

def delete_tesk(request,pk):
	delete_now = Tesk.objects.get(id=pk)
	delete_now.delete()
	messages.success(request, "The Tesk Deleted Succsesfully..")
	return redirect('home')
@login_required
def delete_user_account(request,):
        user =request.user
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('index') 
    
    