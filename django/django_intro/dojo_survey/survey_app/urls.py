from django.urls import path
from . import views
urlpatterns = [
	path('', views.index),
	path('process', views.process),
	path('result', views.result),
	path('random_word', views.random_word),
	path('generate', views.generate),
	path('reset', views.reset),
]