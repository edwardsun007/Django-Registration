from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),### this is going to call the index function under views.py
    url(r'^users$', views.users, name='users'),
    url(r'^all_users$', views.all_users)
]
