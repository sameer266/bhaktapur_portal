from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import MyUser
from ward.models import Ward,Category

def login_ward(request):
    error = None  # Initialize error as None

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Fetch the user by username and password
            user = MyUser.objects.get(username=username, password=password)  # Insecure, better use hashing for passwords.

            # Log the user in
            login(request, user)

            # Redirect to the dashboard after login
            return redirect('dashboard_page')  # Return the redirect response

        except MyUser.DoesNotExist:
            error = "Invalid username or password."

    return render(request, 'pages/login.html', {'error': error})

@login_required
def dashboard(request):
    isSuccess=False
    if request.method=="GET":
        isSuccess=request.GET.get('data')
    ward_no=request.user.ward
    ward_data=Ward.objects.filter(name=ward_no)
    
    return render(request,'dashboard/dashboard.html',{'ward_data':ward_data,'isSuccess':isSuccess})


@login_required
def edit_ward(request, id):
    ward_data = Ward.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('image')

        # Update ward data
        ward_data.title = title
        ward_data.body = body

        # Only update the image if a new one is provided
        if image:
            ward_data.image = image

        # Save the updated data
        ward_data.save()

        # Redirect to the dashboard after editing is successful
        return redirect('/user/dashboard?data=Update Success')

    return render(request, 'dashboard/edit.html', {'ward_data': ward_data})


@login_required
def delete_ward(request,id):
    ward_data=Ward.objects.get(id=id)
    ward_data.delete()
    return redirect('dashboard_page')

@login_required
def add_ward(request):
    ward_no=request.user.ward.name
    category=Category.objects.get(name="Events & Notice")
    if request.method=="POST":
        
        title=request.POST.get('title')
        body=request.POST.get('body')
        image=request.FILES.get('image')
        ward=Ward.objects.create(name=ward_no,title=title,category=category,body=body,image=image)
        ward.save()
        return redirect('/user/dashboard?data=Success Add Data')
        
    return render(request,'dashboard/create.html')
    