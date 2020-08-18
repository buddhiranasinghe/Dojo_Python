from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('add_book', views.add_book),
	path('books/<int:book_id>', views.view_books),
	path('books/<int:book_id>/assign', views.assign_book),
	path('authors', views.authors),
	path('add_author', views.add_author),
	path('authors/<int:author_id>', views.view_authors),
	path('authors/<int:author_id>/assign', views.assign_author),
]