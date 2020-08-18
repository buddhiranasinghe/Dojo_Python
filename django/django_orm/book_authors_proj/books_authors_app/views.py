from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
	context = {
		'books' : Book.objects.all(),
	}
	return render(request, "home.html", context)

def authors(request):
	context = {
		'authors' : Author.objects.all(),
	}
	return render(request, "authors.html", context)

def add_book(request):
	Book.objects.create(
		title = request.POST['title'],
		desc = request.POST['desc'],
	)
	return redirect('/')

def add_author(request):
	print (request.POST['first_name'])
	Author.objects.create(
		first_name = request.POST['first_name'],
		last_name = request.POST['last_name'],
		notes = request.POST['notes']
	)
	return redirect('/authors')

def view_books(request, book_id):
	book = Book.objects.get(id=book_id)
	context = {
		'book' : book,
		'authors' : Author.objects.exclude(id=book_id)
	}
	# print (context["authors"])
	return render(request, "book.html", context)

def view_authors(request, author_id):
	author = Author.objects.get(id=author_id)
	context = {
		'author' : author,
		'books' : Book.objects.exclude(id=author_id)
	}
	return render(request, "author.html", context)

def assign_book(request, book_id):
	# print(f"************{book_id}")
	book = Book.objects.get(id=book_id)
	author = Author.objects.get(id=request.POST['author_id'])
	book.authors.add(author)
	# print("author added")
	return redirect(f"/books/{book_id}")

def assign_author(request, author_id):
	book = Book.objects.get(id=request.POST['book_id'])
	author = Author.objects.get(id=author_id)
	book.authors.add(author)
	return redirect(f"/authors/{author_id}")





