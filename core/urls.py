from . views import home, categories
from django.urls import path

urlpatterns = [
    path('',home, name='home'),
    path('categories/',categories, name='categories')
]