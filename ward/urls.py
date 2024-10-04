
from django.urls import path
from . import views

urlpatterns = [
    path('<id>/',views.getOneWardDetails,name="ward_singlePage_data"),
    

    
    
]