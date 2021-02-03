from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('viewlogin', views.viewlogin),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('create_review', views.create_review),
    path('display_review', views.display_review),
    path('delete/<int:id>', views.delete),
    path('tours', views.tours),
    path('booknow', views.booknow),
]