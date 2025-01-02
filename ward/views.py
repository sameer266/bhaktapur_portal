from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from ward.models import Ward
from user.models import MyUser

# Create your views here.


def getOneWardDetails(request, id):
    # Ensure `id` corresponds to the ward name in MyUser
    user = MyUser.objects.get(ward=1) # Retrieve MyUser by `ward` field

    # Fetch Ward objects linked to the user
    ward = Ward.objects.filter(name=user.ward).order_by('-date_created')
    return render(request, 'ward/ward.html', {'ward_data': ward, 'ward_no': id})
