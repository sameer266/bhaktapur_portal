from django.shortcuts import render
from ward.models import Ward

# Create your views here.

def getOneWardDetails(request,id):
    ward=Ward.objects.filter(name=id).order_by('-date_created')
    return render(request,'ward/ward.html',{'ward_data':ward,'ward_no':id})
