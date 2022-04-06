from django.urls import path
from . import views

urlpatterns = [
    path('',views.front_page,name='front_page'),
    path('register_dvd',views.front_page,name='front_page'),
]