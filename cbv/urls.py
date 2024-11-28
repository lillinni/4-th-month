from django.urls import path
from . import views
urlpatterns = [
    path('create_order/', views.OrderCreateView.as_view(), name='create_order'),
    path('order_list/', views.OrderListView.as_view(), name='order_list'),
    path('order_list/edit/<int:pk>/', views.OrderEditView.as_view(), name='edit_order'),
    path('order_list/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='delete_order'),

]
