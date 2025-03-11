from django.urls import path 
from .import views
urlpatterns=[
    path('',views.home, name='home'),
    path('nos_services/',views.nos_services, name='nos_services'),
]