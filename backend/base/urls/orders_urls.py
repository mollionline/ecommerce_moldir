from django.urls import path

from ..views import order_views as views

urlpatterns = [
    path('add/', views.addOrderItems, name='orders-add'),
    path('<str:pk>/', views.getOrderById, name='user-order'),
]