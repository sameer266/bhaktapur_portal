from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
 path('',views.login_ward,name="login_page"),
 path('dashboard/',views.dashboard,name="dashboard_page"),
 path('dashboard-edit/<id>/',views.edit_ward,name="edit_page"),
 path('dashboard-delete/<id>/',views.delete_ward,name="delete_page"),
 path('dashboard-create/',views.add_ward,name="add_page"),
 
 
    
]