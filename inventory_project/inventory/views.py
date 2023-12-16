from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from .forms import ProductForm

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

from django.shortcuts import render, redirect
from .forms import ProductForm

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def perform_create(self, serializer):
    serializer.save()

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list-create')
    else:
        form = ProductForm()
    
    return render(request, 'create_product.html', {'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class CreateProductView(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                new_product = form.save(commit=False)
                new_product.product_id = None  # Set to None to allow the database to generate a new ID
                new_product.save()
                return JsonResponse({'message': 'Product created successfully'}, status=201)
            else:
                return JsonResponse({'errors': form.errors}, status=400)
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=400)