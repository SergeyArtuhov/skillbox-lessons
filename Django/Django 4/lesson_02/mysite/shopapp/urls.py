from django.contrib import admin
from django.urls import path
from .views import shop_index

app_name = 'shopapp'    # имя приложения

urlpatterns = [
    path('', shop_index, name='index')
]