from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.decorators.cache import cache_page
from .views import (ShopIndexView,
                    GroupsListView,
                    ProductDetailView,
                    ProductsListView,
                    OrderListView,
                    OrderDetailView,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDeleteView,
                    ProductsDataExportView,
                    ProductViewSet)


app_name = 'shopapp'

routers = DefaultRouter()
routers.register("products", ProductViewSet)

urlpatterns = [
    # path('', cache_page(60 * 3)(ShopIndexView.as_view()), name='index'),
    path('', ShopIndexView.as_view(), name='index'),
    path('api/', include(routers.urls)),
    path('groups/', GroupsListView.as_view(), name='groups_list'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/export/', ProductsDataExportView.as_view(), name='products-export'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('orders/', OrderListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_details',)

]