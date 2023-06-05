from timeit import default_timer
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def shop_index(request: HttpRequest):
    context = {
        'time_running': default_timer(),
    }
    return render(request, 'shopapp/shop-index.html', context=context)
