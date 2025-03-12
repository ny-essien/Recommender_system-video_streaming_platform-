from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    
    ##Authentication urls
    path("sign_in/", views.sign_in, name = "sign_in"),
    path("sign_out/", views.sign_out, name = "sign_out"),
    path("register/", views.register, name = "register" ),
    path("reset_password/", views.reset_password, name = "password_reset"),


    path('movies/', views.movies, name='movies'),
    path('tvshows/', views.tvshows, name='tvshows'),
    path('mylist/', views.mylist, name='mylist'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('add-to-list/<int:video_id>/', views.add_to_list, name='add_to_list'),
    path('remove-from-list/<int:video_id>/', views.remove_from_list, name='remove_from_list'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)