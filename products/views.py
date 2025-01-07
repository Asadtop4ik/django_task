from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Product, Category, Order, OrderItem
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListCreateView(ListCreateAPIView, RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer