from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import Group
from timeit import default_timer
from .models import Product, Order, ProductImage
from .forms import GroupForm, ProductForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


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


class ProductDetailView(DetailView):
    template_name = 'shopapp/products-detail.html'
    # model = Product
    queryset = Product.objects.filter(archived=False).prefetch_related("images")  # чтобы архивные продукты не отображались
    context_object_name = "product"


# class ProductDetailView(View):
#     def get(self, request: HttpRequest, pk: int) -> HttpResponse:
#         # product = Product.objects.get(pk=pk)  # так можно, но при вводе несуществующего продукта будет ошибка сервера
#         product = get_object_or_404(Product, pk=pk)  # или вывод продукта из БД или ошибка 404
#         context = {
#             "product": product
#         }
#         return render(request, "shopapp/products-detail.html", context=context)


class ProductsListView(ListView):
    template_name = 'shopapp/products_list.html'
    # model = Product
    queryset = Product.objects.filter(archived=False)  # чтобы архивные продукты не отображались
    context_object_name = "products_list"  # указываем по какой переменной будут передаваться модель в шаблон


# class ProductsListView(TemplateView):
#     template_name = 'shopapp/products_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products_list'] = Product.objects.all()
#         return context


# def products_list(request: HttpRequest):
#     context = {
#         'products_list': Product.objects.all()
#     }
#     return render(request, 'shopapp/products_list.html', context=context)


class ProductCreateView(UserPassesTestMixin, CreateView):
    def test_func(self):
        # return self.request.user.groups.filter(name="secret-group").exists()  #  существует ли такое условие
        return self.request.user.is_superuser  # если пользователь СУПЕР то доступ разрешен

    model = Product
    form_class = ProductForm
    # fields = "name", "price", "description", "discount", "preview"  # или указываем поля, или указываем форму ниже
    # form_class = ProductForm
    success_url = reverse_lazy("shopapp:products_list")  # ссылки можно генерировать только в View функции поэтому так

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.create(
                product=self.object,
                image=image
            )
        return response


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = "name", "price", "description", "discount", "preview"
    template_name_suffix = "_update_form"

    def get_success_url(self):  # генерируем ссылку для возврата к деталям товара
        return reverse(
            "shopapp:product_details",  # ссылка куда переадресовываем
            kwargs={"pk": self.object.pk}  # ссылка на pk обьекта который мы обновили
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.create(
                product=self.object,
                image=image
            )
        return response

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):  # функция выполняется если форма валидна
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


# def product_create(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":  # проверяем какой метод
#         form = ProductForm(request.POST)  # получаем заполненную форму
#         if form.is_valid():  # проверяем валидность формы
#             # name = form.cleaned_data['name'] Clean_data это словарь
#             # price = form.cleaned_data['price']
#             # Product.objects.create(name, price) Можно и так передавать, но это долго
#             # Product.objects.create(**form.cleaned_data)  # распаковываем словарь и передаем в базу данных всю форму
#             form.save()
#             url = reverse('shopapp:products_list')  # генерируем ссылку для перехода
#             return redirect(url)  # открываем ссылку
#     else:  # это если будет Гет запрос
#         form = ProductForm()
#     context = {
#         "form": form
#     }
#     return render(request, 'shopapp/create-product.html', context=context)


# def orders_list(request: HttpRequest):
#     context = {
#         'orders': Order.objects.select_related('user').prefetch_related('products').all(),
#     }  # это значит что необходимо загрузить все объекты Order вместе с пользователями и к ним еще будут присоеденины продукты
#     return render(request, 'shopapp/orders-list.html', context=context)


class OrderListView(LoginRequiredMixin, ListView):
    queryset = Order.objects.select_related('user').prefetch_related('products')  # без all()


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "shopapp.view_order"
    queryset = (Order.objects.select_related('user').prefetch_related('products'))


class ProductsDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.order_by("pk").all()
        products_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": product.price,
                "archived": product.archived
            }
            for product in products
        ]
        return JsonResponse({"products": products_data})
