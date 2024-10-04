from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from content.models import Content,Category
from ward.models import Ward

# Create your views here.


# -----home-------
def Home(request):
    category_culture=Category.objects.get(name="Culture & Tradition")
    culture=Content.objects.filter(category=category_culture).order_by('-date_created')[:4]
    
    category_jobs=Category.objects.get(name="Jobs")
    jobs=Content.objects.filter(category=category_jobs).order_by('-date_created')[:4]
    
    top_news=Content.objects.all().order_by('-date_created')[:6]

    ward=Ward.objects.all().order_by('date_created')[:4]# Fetch only the latest 6 entries
    data={
        'culture_data':culture,
        'jobs_data':jobs,
        'ward_data':ward,
        'top_news':top_news
    }
    return render(request,'pages/home.html',data)


# ---------Jobs------------
def jobDetails(request):
    category_jobs=Category.objects.get(name="Jobs")
    jobs=Content.objects.filter(category=category_jobs)
    return render(request,'pages/jobs.html',{'jobs_data':jobs})


# ------------Culture and Tradition------------
def culture_traditionDetails(request):
    category=Category.objects.get(name="Culture & Tradition")
    culture=Content.objects.filter(category=category)
    return render(request,'pages/culture&trad.html',{'culture_data':culture})

# ---------Events and Notice-------------
def events_noticeDetails(request):
    ward=Ward.objects.all()
    return render(request,'pages/events&notice.html',{'ward_data':ward})

    
# --------  History--------
def historyDetails(request):
    category=Category.objects.get(name="History")
    history=Content.objects.filter(category=category)
    return render(request,'pages/history.html',{'history_data':history})



#--------Expolore places------
def explorePlaces(request):
    
    category=Category.objects.get(name="Explore Places")
    places=Content.objects.filter(category=category)
    
    return render(request,'pages/places.html',{'places_data':places})



# -------search details---------
def serachDetails(request):
 
    query=request.GET.get('query')
    
    data=Content.objects.filter(body__icontains=query)
    return render(request,'pages/searchdetails.html',{'data':data,'query':query})
  
# ----details views when  click in read more ------

def details(request, id):

    try:
        ward=Ward.objects.get(slug=id)
        return render(request,'pages/details.html',{'data':ward})
    except Exception as e:
        content=Content.objects.get(id=id)
        return render(request,'pages/details.html',{'data':content})