from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('devops/', views.devops, name='devops'),
    path('blogs/', views.blogs, name='blogs'),
]
