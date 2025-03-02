
from django.urls import path
from . import views

urlpatterns = [
    path('<name>/',views.getOneWardDetails,name="ward_singlePage_data"),
    

    
    
]