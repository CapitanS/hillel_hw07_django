from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='products/', permanent=True)),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/create/', views.ProductCreate.as_view(), name='product-create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
    path('customers_price/', cache_page(5 * 60)(views.CustomerPriceListView.as_view()), name='customer-order-price'),
]
