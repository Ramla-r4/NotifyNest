from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from.models import Tesk
from .forms import OrginazeTesk
from django.contrib.auth.decorators import login_required

def home(request):
	tesks = Tesk.objects.all()
	return render(request, 'All/index.html', {'tesks':tesks})


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		if User.objects.filter(username=username).exists():
			messages.info(request, 'Username Taked')
			return redirect('login')
		else:
			user1 =User.objects.create_user(username=username,password=password)
			user1.save()
	else:
	  return render(request, 'All/login.html')



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('index')


def add_tesk(request):
	form = OrginazeTesk(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_tesk=form.save()
				messages.success(request, "Record Added...")
				return redirect('index')
		return render(request, 'All/add_tesk.html', {'form':form})
	else:
		messages.success(request, "You Need to Sign Up to Orginaze You Tesk")
		return redirect('index')
		

def delete_tesk(request,pk):
	delete_now = Tesk.objects.get(id=pk)
	delete_now.delete()
	messages.success(request, "the tesk deleted succsesfully")
	return redirect('index')

