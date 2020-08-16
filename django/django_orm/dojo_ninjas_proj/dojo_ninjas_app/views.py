from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
	context = {
		'all_dojos' : Dojo.objects.all(),
	}
	return render(request, "home.html", context)


def add_dojo(request):
	Dojo.objects.create(
		name=request.POST['name'],
		city=request.POST['city'],
		state=request.POST['state'],
	)
	return redirect('/')


def add_ninja(request):
	Ninja.objects.create(
		first_name=request.POST['fname'],
		last_name=request.POST['lname'],
		dojo_id=request.POST['dojo'],
	)
	return redirect('/')


