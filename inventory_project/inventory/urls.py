# inventory/urls.py

from django.urls import path
from .views import ProductListCreateView, ProductDetailView,ProductUpdateView,ProductDeleteView,create_product,CreateProductView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('create-product/', CreateProductView.as_view(), name='create-product'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
