from django.urls import path 
from .import views
urlpatterns=[
    path('',views.home, name='home'),
    path('nos_services/',views.nos_services, name='nos_services'),
    
    path('create/',views.create_student, name='create_student'),
    
    path('edit/<int:id>/',views.edit_student, name='edit_student'),
    
    path('delete/<int:id>/',views.delete_student, name='delete_student'),
]