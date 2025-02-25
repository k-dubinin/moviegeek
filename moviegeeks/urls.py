from django.urls import path, re_path

from moviegeeks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    re_path(r'^genre/(?P<genre_id>[\w-]+)/$', views.genre, name='genre'),
    path('search/', views.search_for_movie, name='search_for_movie'),
]
