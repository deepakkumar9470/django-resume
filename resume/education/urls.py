from django.urls import path
from . import views
urlpatterns = [
    path('myskill/',views.skill_set,name='Skills'),
   
]