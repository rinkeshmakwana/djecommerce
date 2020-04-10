from django.urls import path
from .views import (
    HomeView,
    ProductDetailView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    remove_single_product_from_cart,
    CheckoutView,
    PaymentView
)

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-product-from-cart/<slug>/', remove_single_product_from_cart, name='remove-single-product-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
]
