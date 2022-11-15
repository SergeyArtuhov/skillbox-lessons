from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Advertisement
from random import sample



def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement.html', {})


def advertisement_detail(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    advertisements = sample(advertisements, 1)
    return render(request, 'advertisement/detail.html', {'advertisements': advertisements})


def advertisement_contacts(request, *args, **kwargs):
    tel = '+79782345543'
    e_mail = 'contacts@mail.com'
    return render(request, 'advertisement/contacts.html', {'tel': tel, 'e_mail': e_mail})


def advertisement_about(request, *args, **kwargs):
    title = 'Бесплатные объявления'
    descr = 'Бесплатные объявления в вашем городе'
    return render(request, 'advertisement/about.html', {'title': title, 'descr': descr})


def advertisement_categories(request, *args, **kwargs):
    categories_list = [
        'Личные вещи', 'Транспорт', 'Хобби'
    ]
    return render(request, 'advertisement/categories.html', {'cat_list': categories_list})


# def advertisement_regions(request, *args, **kwargs):
#     reg_list = [
#         'Москва', 'Санкт-Петербург', 'Крым'
#     ]
#     return render(request, 'advertisement/regions.html', {'reg_list': reg_list})


class AdvertisementRegions(View):

    def get(self, request):
        reg_list = [
            'Москва', 'Санкт-Петербург', 'Крым'
        ]
        return HttpResponse(reg_list)

    def post(self, request):
        return HttpResponse('Регион успешно создан')