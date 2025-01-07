from rest_framework import serializers
from .models import Category, Product, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'created_at', 'updated_at']


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_name', 'product_price', 'quantity', 'created_at', 'updated_at']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'customer_email', 'created_at', 'updated_at', 'total_price', 'items']

    def get_total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())

    def update(self, instance, validated_data):
        instance.calculate_total_price()
        return super().update(instance, validated_data)
