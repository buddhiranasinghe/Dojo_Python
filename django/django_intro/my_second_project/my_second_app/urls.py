from django.urls import path
from . import views
urlpatterns = [
	path('', views.index),
	path('bears', views.my_method),
	path('bears/<int:my_val>', views.jam_method),
	path('bears/<str:poke>/poke', views.yet_another),
	path('<int:id>/<str:color>', views.one_more),
	path('index', views.index),
]