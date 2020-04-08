from django.urls import path
from .views import checkout
from .views import HomeView, ProductDetailView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>', ProductDetailView.as_view(), name='product'),
    path('', checkout, name='checkout'),
]
