from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import MyUser
from ward.models import Ward, Category

def login_ward(request):
    error = None  # Initialize error as None

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Fetch the user by username and password
            user = MyUser.objects.get(username=username)
            
            if user.check_password(password):  # Using password hashing for security
                login(request, user)  # Log the user in

                # Redirect to the dashboard after login
                return redirect('dashboard_page')  # Return the redirect response
            else:
                error = "Invalid username or password."
        
        except MyUser.DoesNotExist:
            error = "Invalid username or password."

    return render(request, 'pages/login.html', {'error': error})


@login_required
def dashboard(request):
    isSuccess = False
    if request.method == "GET":
        isSuccess = request.GET.get('data')

    # Retrieve the ward associated with the logged-in user
    ward_no = request.user.ward  # Ward name from MyUser
    ward_data = Ward.objects.filter(name__ward=ward_no)  # Filter Ward by the user's ward

    return render(request, 'dashboard/dashboard.html', {'ward_data': ward_data, 'isSuccess': isSuccess})


@login_required
def edit_ward(request, id):
    ward_data = get_object_or_404(Ward, id=id)

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
def delete_ward(request, id):
    ward_data = get_object_or_404(Ward, id=id)
    ward_data.delete()
    return redirect('dashboard_page')


@login_required
def add_ward(request):
    # Get the ward name of the logged-in user
    ward_no = request.user.ward  # Ward name from MyUser
    category = Category.objects.get(name="Events & Notice")

    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('image')

        # Create a new ward entry and link it to the user's ward
        ward = Ward.objects.create(
            name=request.user,  # Link to the MyUser object
            title=title,
            category=category,
            body=body,
            image=image
        )
        ward.save()
        return redirect('/user/dashboard?data=Success Add Data')

    return render(request, 'dashboard/create.html')
