from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderListCreateView, OrderItemViewSet, CategoryListCreateView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'order-items', OrderItemViewSet, basename='orderitem')


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('', include(router.urls)),
]
