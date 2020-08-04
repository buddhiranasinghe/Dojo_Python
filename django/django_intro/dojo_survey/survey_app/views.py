from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
	return render(request, 'form.html')

# def process(request):
# 	if request.method == 'POST':
# 		print(request.POST)
# 		context = {
# 			'name': request.POST['user_name'],
# 			'location': request.POST['location'],
# 			'language': request.POST['fav_lang'],
# 			'gender': request.POST['gender'],
# 			'duration': request.POST['duration'],
# 			'comment': request.POST['comment']
# 		}
# 		return render(request, 'result.html', context)
# 	return render(request, 'result.html')


def process(request):
	print(request.POST)
	request.session['name'] = request.POST['user_name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['fav_lang']
	request.session['gender'] = request.POST['gender']
	request.session['duration'] = request.POST['duration']
	request.session['comment'] = request.POST['comment']
	return redirect('/result')

def result(request):
	return render(request, "result.html")

def random_word(request):
	if 'attempt_count' not in request.session:
		request.session['attempt_count'] = 0
	request.session['attempt_count'] += 1
	request.session['random_word'] = get_random_string(length=14)
	return render(request, "random_word.html")

def generate(request):
	request.session['attempt_count'] += 1
	request.session['random_word'] = get_random_string(length=14)
	return render(request, "random_word.html")

def reset(request):
	request.session.flush()
	return redirect('/random_word')


















