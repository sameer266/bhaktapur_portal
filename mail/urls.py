from django.urls import path
from mail import views



urlpatterns = [
    path('email-form/',views.send_email_view,name="email_form" ),
         
]