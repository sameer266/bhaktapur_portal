from content.models import Category
from ward.models import Ward

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def wards(request):
    wards = Ward.objects.all()
    return {'wards': wards}