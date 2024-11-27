from django.urls import path
from . import views 

urlpatterns = [
    path('all_clothes/', views.all_clothes_view, name='all_clothes_tags'),
    path('older/', views.older_view, name='older_tags'),
    path('younger/', views.younger_view, name='younger_tags'),
    path('kids/', views.kids_view, name='kids_tags'),


]