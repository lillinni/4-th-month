from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.views import generic
from . import models
from .models import Book


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Привет! Меня зовут Элина, рада знакомству.')


def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse(
            'Привет! Это мой питомец, его зовут Артси. '
            '<img src="https://png.pngtree.com/png-vector/20230912/ourmid/pngtree-3d-cute-cat-isolated-png-image_10024929.png">'
        )


def system_time(request):
    if request.method == 'GET':
        current_time = datetime.now()
        return HttpResponse(f"Текущие дата и время: {current_time}")


class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_detail'
    model = Book

    def get_object(self, queryset=None):
        book_id = self.kwargs.get('book_id')  
        return get_object_or_404(Book, id=book_id)


class BookSearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return models.Book.objects.filter(title__icontains=query).order_by('-id')
        return models.Book.objects.none()  # Возвращает пустой QuerySet, если запрос пуст.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

# def book_list_view(request):
#     if request.method == 'GET':
#         book_list = models.Book.objects.filter().order_by('-id')  
#         context = {'book_list': book_list}
#         return render(request, template_name='book.html', context=context)


# def book_detail_view(request, book_id):
#     if request.method == 'GET':
#         book_detail = get_object_or_404(models.Book, id=book_id)  
#         context = {'book_detail': book_detail}
#         return render(request, template_name='book_detail.html', context=context) 

