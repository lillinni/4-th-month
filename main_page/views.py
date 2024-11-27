from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

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


def book_list_view(request):
    if request.method == 'GET':
        book_list = models.Book.objects.filter().order_by('-id')  
        context = {'book_list': book_list}
        return render(request, template_name='book.html', context=context)

def book_detail_view(request, book_id):
    if request.method == 'GET':
        book_detail = get_object_or_404(models.Book, id=book_id)  
        context = {'book_detail': book_detail}
        return render(request, template_name='book_detail.html', context=context) 
