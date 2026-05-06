from django.urls import path

from . import views

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('doctors/', views.doctors, name='doctors'),
path('services/', views.services, name='services'),
path('blog/', views.blog, name='blog'),
path('blog_single/', views.blog_single, name='blog_single'),
]