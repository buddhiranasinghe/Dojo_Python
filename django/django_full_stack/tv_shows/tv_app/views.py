from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def shows(request):
	context = {
		'shows' : Show.objects.all()
	}
	return render (request, "shows.html", context)

def new_shows(request):
	return render (request, "new.html")

def create(request):
	if request.method == 'POST':
		# print(request.POST)
		Show.objects.create(
			title = request.POST['title'],
			network = request.POST['network'],
			release_date = request.POST['release_date'],
			description = request.POST['description']
		)
		return redirect ('/shows')

def view_show(request, show_id):
	one_show = Show.objects.get(id=show_id)
	context = {
		'show' : one_show
	}
	return render (request, "view_show.html", context)

def edit_show(request, show_id):
	one_show = Show.objects.get(id=show_id)
	context = {
		'show' : one_show
	}
	return render (request, "edit_shows.html", context)

def update_show(request, show_id):
	print(request.POST)
	one_update = Show.objects.get(id=show_id)
	one_update.title = request.POST['title']
	one_update.network = request.POST['network']
	one_update.release_date = request.POST['release_date']
	one_update.description = request.POST['description']
	one_update.save()
	return redirect ('/shows')

def delete_show(request, show_id):
	one_delete = Show.objects.get(id=show_id)
	one_delete.delete()
	return redirect ('/shows')


