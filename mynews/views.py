from django.shortcuts import render, get_object_or_404,redirect
from content.models import Content, Category
from ward.models import Ward
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# ---logout-----
@csrf_exempt
def logoutUser(request):
    logout(request)
    return redirect('/')
    
# ----home page-----
def Home(request):
    
    categories = Category.objects.all()


    category_culture = Category.objects.get(name="Culture & Tradition")
    culture = Content.objects.filter(category=category_culture).order_by('-date_created')[:6]
    
    category_jobs = Category.objects.get(name="Jobs")
    jobs = Content.objects.filter(category=category_jobs).order_by('-date_created')[:4]
    
  
    top_news = Content.objects.all().order_by('-date_created')[:6]

    ward_data = Ward.objects.all().order_by('date_created')[:4]  # Adjust this query based on your requirements

    data = {
        'culture_data': culture,
        'jobs_data': jobs,
        'ward_data': ward_data,
        'top_news': top_news,
        'categories': categories,  
    }

    return render(request, 'pages/home.html', data)


# ---------Jobs------------
def jobDetails(request):
    category_jobs = Category.objects.get(name="Jobs")
    jobs = Content.objects.filter(category=category_jobs)
    return render(request, 'pages/jobs.html', {'jobs_data': jobs})


# ------------Culture and Tradition------------
def culture_traditionDetails(request):
    category = Category.objects.get(name="Culture & Tradition")
    culture = Content.objects.filter(category=category)
    return render(request, 'pages/culture&trad.html', {'culture_data': culture})


# ---------Events and Notice-------------
def events_noticeDetails(request):
    ward_data = Ward.objects.all().order_by('date_created')
    return render(request, 'pages/events&notice.html', {'ward_data': ward_data})


# --------  History--------
def historyDetails(request):
    category = Category.objects.get(name="History")
    history = Content.objects.filter(category=category)
    return render(request, 'pages/history.html', {'history_data': history})


# --------Expolore places------
def explorePlaces(request):
    category = Category.objects.get(name="Explore Places")
    places = Content.objects.filter(category=category)
    return render(request, 'pages/places.html', {'places_data': places})


# -------More category details--------
def categoryDetails(request, id):
    category = Category.objects.get(id=id)
    data = Content.objects.filter(category=category)
    return render(request, 'pages/categorydetails.html', {'data': data, 'category': category})

# -------search details---------
def searchDetails(request):
    query = request.GET.get('query')
    data = Content.objects.filter(body__icontains=query)
    return render(request, 'pages/searchdetails.html', {'data': data, 'query': query})
  

# ----details views when click on read more------
def details(request, id):
    try:
        print(id)
        # Attempt to retrieve a Ward object if it exists
        ward = Ward.objects.get( id=id)
        return render(request, 'pages/details.html', {'data': ward})
    except:
        # If no Ward object is found, retrieve a Content object instead
        content = get_object_or_404(Content, id=id)
        return render(request, 'pages/details.html', {'data': content})
