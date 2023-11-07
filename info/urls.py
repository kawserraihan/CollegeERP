from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    
    path('initialize_days_of_week/', views.initialize_days_of_week, name='initialize_days_of_week'),

    path('departments/', views.DepartmentList, name='departments'),
]



