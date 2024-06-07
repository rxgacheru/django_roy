from django.urls import path
from .views import *
from . import views

urlpatterns = [
  path('', index, name='index'),
  path('about/', about, name='about'),
  path('contact/', contact, name='contact'),
  path('bloglist/',blog_list, name='bloglist'),
  path('subscribe/', views.subscribe, name='subscribe'),
]