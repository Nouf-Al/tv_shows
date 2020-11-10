from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('shows', views.all_shows, name="all_shows"),
    path('shows/new', views.new_show, name="new_show"),
    path('shows/create', views.create_show, name="create_show"),
    path('shows/<int:id>', views.view_show, name="view_show"),
    path('shows/<int:id>/delete', views.delete_show, name="delete_show"),
    path('shows/<int:id>/edit', views.edit_show, name="edit_show"),
    path('shows/<int:id>/update_show', views.update_show, name="update_show"),

    





]
