from django.shortcuts import render
from . models import Link, Category

# Create your views here.
def home(request):
    context = {
        'links' : Link.objects.all(),
        'categories' : Category.objects.all()
    }
    return render(request, 'core/home.html', context)

def categories(request):
    return render(request, 'core/categories.html')
