# inventory/serializers.py

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


    read_only_fields = ['id']  # Make 'id' read-only to avoid client-side manipulation