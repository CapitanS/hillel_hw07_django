from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from orders.models import Product


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
    fields = '__all__'  # Not recommended (potential security issue if more fields added)


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products')
