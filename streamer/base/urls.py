from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path("login/", views.login, name = "login"),
    path('movies/', views.movies, name='movies'),
    path('tvshows/', views.tvshows, name='tvshows'),
    path('mylist/', views.mylist, name='mylist'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('add-to-list/<int:video_id>/', views.add_to_list, name='add_to_list'),
    path('remove-from-list/<int:video_id>/', views.remove_from_list, name='remove_from_list'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)