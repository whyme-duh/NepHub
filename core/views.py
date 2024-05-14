from django.shortcuts import render
from . models import Link, Category
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    context = {
        'links' : Link.objects.all(),
        'categories' : Category.objects.all()
    }
    return render(request, 'core/home.html', context)



def categories(request):
    return render(request, 'core/categories.html', {"categories": Category.objects.all()})


def categories_detail(request, slug):
    links_list = Link.objects.filter(category = Category.objects.get(slug= slug))
    return render(request, 'core/detail_page.html', {"links": links_list})

    
