from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "pk",
            "name",
            "description",
            "price",
            "discount",
            "archived",
            "created_at",
            "preview",
        )
