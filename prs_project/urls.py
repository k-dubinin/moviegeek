"""prs_project URL Configuration"""
from django.urls import include, path, re_path
from django.contrib import admin
from moviegeeks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', include('moviegeeks.urls')),
    path('collect/', include('collector.urls')),
    path('analytics/', include('analytics.urls')),
    re_path(r'^admin/', admin.site.urls),
    path('rec/', include('recommender.urls'))
]
