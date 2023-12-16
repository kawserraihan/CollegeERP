from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *


urlpatterns = [
    path('',views.index, name='index'),
    path('access-denied/', views.access_denied, name='access_denied'),
    
    path('initialize_days_of_week/', views.initialize_days_of_week, name='initialize_days_of_week'),
    path('get_departments/', views.get_departments, name='get_departments'),

    path('days/', views.DaysList, name='days'),
    path('add_days/', views.AddDays, name='add_days'),
    path('edit_days/<int:pk>/', views.EditDays, name='edit_days'),
    path('delete_days/<int:pk>/', views.DeleteDays, name='delete_days'),

    path('departments/', views.DepartmentList, name='departments'),
    path('add_department/', views.AddDepartment, name='add_department'),
    path('edit_department/<int:pk>/', views.EditDepartment, name='edit_department'),
    path('delete_department/<int:pk>/', views.DeleteDepartment, name='delete_department'),

    path('users/', views.UserList, name = 'userlist'),
    path('toggle_user_active_status/<int:user_id>/', views.toggle_user_active_status, name='toggle_user_active_status'),
    path('users/add', views.AddUser, name='useradd'),
    path('users/edit/<int:id>/', views.EditUser, name = 'useredit'),
    path('users/delete/<int:id>/', views.DeleteUser, name = 'userdelete'),
    
    path('bus/shuttles', views.ShuttleBus, name = 'shuttle_bus'),
]




