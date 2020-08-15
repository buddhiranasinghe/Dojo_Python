from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def root(request):
	context = {
		'users' : User.objects.all(),
	}
	return render(request, "home.html", context)


def add_user(request):
	User.objects.create(
		first_name = request.POST['fname'],
		last_name = request.POST['lname'],
		email = request.POST['email'],
		age = request.POST['age'],
		created_at = models.DateTimeField(auto_now_add=True),
		updated_at = models.DateTimeField(auto_now=True),
	)
	return redirect ('/')

