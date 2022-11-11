from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement.html', {})


def advertisement_detail(request, *args, **kwargs):
    return HttpResponse('Тут какие-то детали')
