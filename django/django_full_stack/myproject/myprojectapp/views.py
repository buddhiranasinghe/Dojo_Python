from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
	context = {
		'all_reviews' : Reviews.objects.all()
	}
	return render(request, "home.html", context)

def viewlogin(request):
	return render(request, "login.html")

def register(request):
	if request.method == 'POST':
		errors = User.objects.validator(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)
			return redirect('/')
		new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
		request.session['name'] = new_user.first_name + ' ' + new_user.last_name
		request.session['user_id'] = new_user.id
		return redirect('/')
	return redirect('/')

def login(request):
	if request.method == 'POST':
		logged_user = User.objects.filter(email=request.POST['email'])
		if len(logged_user) > 0:
			logged_user = logged_user[0]
			if logged_user.password == request.POST['password']:
				request.session['name'] = logged_user.first_name + ' ' + logged_user.last_name
				request.session['user_id'] = logged_user.id
				return redirect('/')
	return redirect('/')

def create_review(request):
	if request.method == 'POST':
		errors = User.objects.review_validation(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)
			return redirect('/')
		new_review = Reviews.objects.create(review = request.POST['new_review'], creator = User.objects.get(id=request.session['user_id']))
	return redirect ('/display_review')

def display_review(request):
	context = {
		'all_reviews' : Reviews.objects.all()
	}
	return render(request, 'home.html', context)

def delete(request, id):
	one_delete = Reviews.objects.get(id=id)
	one_delete.delete()
	return redirect ('/')

def tours(request):
	return render(request, "tours.html")

def booknow(request):
	if request.method == 'POST':
		request.session['full_name'] = request.POST['full_name']
		request.session['email'] = request.POST['email']
		request.session['country'] = request.POST['country']
		request.session['arrival_date'] = request.POST['arrival_date']
		request.session['pickup_place'] = request.POST['pickup_place']
		return render(request, "confirm.html")
	return redirect('/tours')

def logout(request):
	request.session.flush()
	return redirect('/')

# def login(request):
# 	return render (request, "login.html")

# def register(request):
# 	return render (request, "register.html")

