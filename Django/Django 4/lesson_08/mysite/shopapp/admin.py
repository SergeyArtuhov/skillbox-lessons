from io import TextIOWrapper
from csv import DictReader

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from .models import Product, Order, ProductImage
from .admin_mixins import ExportAsCSVMixin
from .forms import CSVImportForm


class OrderInline(admin.TabularInline):  # добавили связь продукта с заказом
    model = Product.orders.through


class ProductImagesInline(admin.StackedInline):
    model = ProductImage


@admin.action(description='Archive products')  # действие для архивирования выбранных продуктов
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description='Unarchive products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)  # вместо декоратора - admin.site.register(Product, ProductAdmin)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):  # подмешали миксин
    change_list_template = "shopapp/products_changelist.html"

    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv',
    ]
    inlines = [
        OrderInline,
        ProductImagesInline,
    ]
    list_display = 'pk', 'name', 'description_short', 'price', 'discount', 'archived'
    list_display_links = 'pk', 'name'  # ссылки
    ordering = 'name', 'pk'  # сортировка
    search_fields = 'name', 'description'  # поиск по полям
    fieldsets = [  # отображение полей
        (None, {  # группа полей без названия с полями name и description
            'fields': ('name', 'description'),
        }),
        ('Price options', {  # группа полей price options с полями price и discount но будет скрыта изначально
            'fields': ('price', 'discount'),
            'classes': ('collapse', 'wide'),
        }),
        ('Images', {  # группа полей price options с полями price и discount но будет скрыта изначально
            'fields': ('preview',)
        }),
        ('Extra options', {
            'fields': ('archived',),
            'classes': ('collapse',),
            'description': 'Extra options. Field "archived" is for soft delete'
        })

    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'

    def import_csv(self, request: HttpRequest) -> HttpResponse:
        if request.method == "GET":
            form = CSVImportForm()
            context = {
                "form": form
            }
            return render(request, "admin/csv_form.html", context)
        form = CSVImportForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {
                "form": form
            }
            return render(request, "admin/csv_form.html", context, status=400)

        csv_file = TextIOWrapper(
            form.files["csv_file"].file,
            encoding=request.encoding
        )

        reader = DictReader(csv_file)

        products = [
            Product(**row)
            for row in reader
        ]

        Product.objects.bulk_create(products)
        self.message_user(request, "Data from CSV was imported")
        return redirect("..")

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path(
                "import-product-csv/",
                self.import_csv,
                name='import_products_csv'
            ),
        ]
        return new_urls + urls


# class ProductInline(admin.TabularInline):
class ProductInline(admin.StackedInline):
    model = Order.products.through  # through указывает что продукты нужно вытащить через заказ


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = 'delivery_address', 'promocode', 'created_at', 'user_verbose'

    def get_queryset(self, request):  # оптимизируем запрос к базе данных чтобы все пользователи загружались
        # с одного запроса, а не каждый раз при загрузке заказа
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbose(self, obj: Order) -> str:  # выводим имя юзера вместо юзернейма
        return obj.user.first_name or obj.user.username