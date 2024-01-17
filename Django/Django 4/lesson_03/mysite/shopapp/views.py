from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import Group
from timeit import default_timer
from .models import Product


def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 999),
        ('Desktop', 1999),
        ('Iphone', 2999),
    ]

    context = {
        'time_running': default_timer(),
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        'products_list': Product.objects.all()
    }
    return render(request, 'shopapp/products_list.html', context=context)