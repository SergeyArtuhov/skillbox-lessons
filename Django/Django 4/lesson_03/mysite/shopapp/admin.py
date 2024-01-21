from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from .models import Product, Order
from .admin_mixins import ExportAsCSVMixin


class OrderInline(admin.TabularInline):  # добавили связь продукта с заказом
    model = Product.orders.through


@admin.action(description='Archive products')  # действие для архивирования выбранных продуктов
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description='Unarchive products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)  # вместо декоратора - admin.site.register(Product, ProductAdmin)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):  # подмешали миксин
    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv',
    ]
    inlines = [
        OrderInline,
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