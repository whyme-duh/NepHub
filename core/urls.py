from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('categories/', views.categories, name = "categories"),
    path('<slug:slug>/', views.categories_detail, name = "detail-page"),
]