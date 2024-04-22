from django.urls import path
from . import views

urlpatterns = [
    path('med_info/', views.med_info, name='med_info'),
]