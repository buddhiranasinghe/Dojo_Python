from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
	return render(request, 'index.html')

def new(request):
	return render(request, 'new.html')

def create(request):
	return redirect('/')

def show(request, number):
	return HttpResponse(f"placeholder to display blog: {number}")

def edit(request, number):
	return HttpResponse(f"placeholder to edit blog: {number}")

def destroy(request, number):
	return HttpResponse(f"This is a placeholder to delete blog: {number}")
