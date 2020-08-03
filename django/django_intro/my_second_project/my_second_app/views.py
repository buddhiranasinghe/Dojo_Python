from django.shortcuts import render, HttpResponse
def index(request):
	return HttpResponse ("This is my response")

def my_method(request):
	return HttpResponse("This is my method Second Method")

def jam_method(request,my_val):
	return HttpResponse(f"This is my 3rd page {my_val}")

def yet_another(request,poke):
	return HttpResponse(f"check this out {poke}")

def one_more(request,id,color):
	return HttpResponse(f"This is page number {id} and color is {color}")

def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

# Create your views here.
