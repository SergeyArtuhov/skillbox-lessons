from timeit import default_timer
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 999),
        ('Desktop', 1999),
        ('Iphone', 2999),
    ]
    context = {
        'time_running': default_timer(),
        'products': products
    }
    return render(request, 'shopapp/shop-index.html', context=context)
