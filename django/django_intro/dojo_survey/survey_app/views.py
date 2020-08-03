from django.shortcuts import render, redirect

def index(request):
	return render(request, 'form.html')

def process(request):
	print(request.POST)
	request.session['name'] = request.POST['user_name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['fav_lang']
	request.session['gender'] = request.POST['gender']
	# request.session['duration'] = request.POST['duration']
	request.session['comment'] = request.POST['comment']
	return redirect('/result')

def result(request):
	return render(request, "result.html")

# Create your views here.
