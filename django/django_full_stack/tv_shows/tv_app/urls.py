from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('shows', views.shows),
    path('shows/new', views.new_shows),
    path('shows/create', views.create),
    path('shows/<int:show_id>', views.view_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.update_show),
    path('shows/<int:show_id>/delete', views.delete_show),
]