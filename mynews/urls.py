"""
URL configuration for mynews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home_page'),
    path('jobs/',views.jobDetails,name="job_page"),
    path('culture-tradition/',views.culture_traditionDetails,name="culture_page"),
    path('history/',views.historyDetails,name="history_page"),
    path('events-notice/',views.events_noticeDetails,name="event_page"),
    path('explore-places/',views.explorePlaces,name="explore_page"),
    path('search-details/',views.serachDetails,name="search-page"),
    path('details/<id>',views.details,name="details_page"),


      path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path('ward/',include('ward.urls')),
    path('user/',include('user.urls')),
    
]


# This will serve media files during development
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)