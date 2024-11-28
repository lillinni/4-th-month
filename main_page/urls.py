from django.urls import path
from . import views
from .views import BookSearchView

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('books/<int:book_id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('search/', BookSearchView.as_view(), name='book_search'),

]
