from django.urls import path
from .views import shop_index, groups_list, products_list, orders_list, product_create


app_name = 'shopapp'

urlpatterns = [
    path('', shop_index, name='index'),
    path('groups/', groups_list, name='groups_list'),
    path('products/', products_list, name='products_list'),
    path('products/create/', product_create, name='product_create'),
    path('orders/', orders_list, name='orders_list')

]