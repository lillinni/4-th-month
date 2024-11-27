from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('orders/', views.order_list, name='order_list'),
    path('edit/<int:order_id>/', views.edit_order, name='edit_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
]
