from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement/detail/', views.advertisement_detail, name='advertisement_detail'),
    path('contacts/', views.advertisement_contacts, name='advertisement_contacts'),
    path('about/', views.advertisement_about, name='advertisement_about'),
    path('categories/', views.advertisement_categories, name='advertisement_categories'),
    path('regions/', views.AdvertisementRegions.as_view())
]