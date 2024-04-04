from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import Group
from timeit import default_timer
from .models import Product, Order
from .forms import GroupForm, ProductForm
from django.views import View


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
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


# def shop_index(request: HttpRequest):
#     products = [
#         ('Laptop', 999),
#         ('Desktop', 1999),
#         ('Iphone', 2999),
#     ]
#     context = {
#         'time_running': default_timer(),
#         'products': products
#     }
#     return render(request, 'shopapp/shop-index.html', context=context)


class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupForm,
            'groups': Group.objects.prefetch_related('permissions').all()
        }
        return render(request, 'shopapp/groups-list.html', context=context)

    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        # return self.get(request) так можно но нежелательно
        return redirect(request.path)  # возвращаем путь на эту же страницу


# def groups_list(request: HttpRequest):
#     context = {
#         'groups': Group.objects.prefetch_related('permissions').all(),
#     }
#     return render(request, 'shopapp/groups-list.html', context=context)


class ProductDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        # product = Product.objects.get(pk=pk)  # так можно, но при вводе несуществующего продукта будет ошибка сервера
        product = get_object_or_404(Product, pk=pk)  # или вывод продукта из БД или ошибка 404
        context = {
            "product": product
        }
        return render(request, "shopapp/products-detail.html", context=context)


def products_list(request: HttpRequest):
    context = {
        'products_list': Product.objects.all()
    }
    return render(request, 'shopapp/products_list.html', context=context)


def product_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":  # проверяем какой метод
        form = ProductForm(request.POST)  # получаем заполненную форму
        if form.is_valid():  # проверяем валидность формы
            # name = form.cleaned_data['name'] Clean_data это словарь
            # price = form.cleaned_data['price']
            # Product.objects.create(name, price) Можно и так передавать, но это долго
            # Product.objects.create(**form.cleaned_data)  # распаковываем словарь и передаем в базу данных всю форму
            form.save()
            url = reverse('shopapp:products_list')  # генерируем ссылку для перехода
            return redirect(url)  # открываем ссылку
    else:  # это если будет Гет запрос
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request, 'shopapp/create-product.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all(),
    }  # это значит что необходимо загрузить все объекты Order вместе с пользователями и к ним еще будут присоеденины продукты
    return render(request, 'shopapp/orders-list.html', context=context)
