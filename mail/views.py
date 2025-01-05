from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from user.models import MyUser
from django.contrib.auth.decorators import login_required

@login_required
def send_email_view(request):
    # Collect ward officers with username and email
    ward_officers = MyUser.objects.filter(role="ward_officer").values('username', 'email')

    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        address = request.POST.getlist('address')

        # If "Select All" is selected, send to all emails
        if "all" in address:
            address = [officer['email'] for officer in ward_officers]

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, address)
            messages.success(request, "Email sent successfully!")
        except Exception as e:
            messages.error(request, f"Error in sending email: {e}")

        return render(request, "admin/email.html", {'officers': ward_officers, 'messages': messages.get_messages(request)})

    return render(request, "admin/email.html", {'officers': ward_officers})
