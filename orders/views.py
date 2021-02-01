from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import FloatField, Sum
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from orders.models import Customer, Product


# Create your views here.
class ProductListView(generic.ListView):
    """Generic class-based view for a list of author."""
    model = Product
    paginate_by = 2


class ProductDetailView(generic.DetailView):
    """Generic class-based view for a product."""
    model = Product


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'price']


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'price']


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products')


class CustomerPriceListView(ListView):
    model = Customer
    template_name = 'orders/customers_price_list.html'
    context_object_name = 'customers'
    paginate_by = 100
    queryset = Customer.objects.all().annotate(order_price=Sum('product__price', output_field=FloatField()))
