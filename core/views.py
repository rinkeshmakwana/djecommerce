from django.shortcuts import render, get_object_or_404
from .models import Product, OrderProduct
from django.views.generic import ListView, DetailView


def checkout(request):
    return render(request, "checkout.html")


# class based view
class HomeView(ListView):
    model = Product
    template_name = 'home.html'


# function based view
# def home(request):
#     context = {
#         'products': Product.objects.all()
#     }
#     return render(request, "home.html", context)


# class based view
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products.html'


# function based view
# def products(request):
#     context = {
#         'products': Product.objects.all()
#     }
#     return render(request, "products.html", context)

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_product = OrderProduct.objects.create(product=product)

