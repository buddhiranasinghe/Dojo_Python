from django.shortcuts import render

def root(request):
	return render(request, "home.html")


# Create your views here.
