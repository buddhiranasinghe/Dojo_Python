from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.

def index(request):
	if "gold" not in request.session:
		request.session['gold'] = 0
	return render(request, 'gold.html')

def process_gold(request):
	print (request.POST)
	if "farm" in request.POST:
		gold = int(random.random() * 10 + 10)
		request.session['gold'] += gold
	if "cave" in request.POST:
		gold = int(random.random() * 5 + 5)
		request.session['gold'] += gold
	if "house" in request.POST:
		gold = int(random.random() * 3 + 2)
		request.session['gold'] += gold
	if "casino" in request.POST:
		gold = int(random.random() * 50 + 0)
		if int(random.random() * 10) > 5:
			# gain gold
			request.session['gold'] += gold
		else:
			# loose gold
			request.session['gold'] -= gold
	return redirect('/')

def reset(request):
	request.session.flush()
	return redirect('/')



