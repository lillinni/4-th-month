from django.shortcuts import render
from . import models

def all_clothes_view(request):
    if request.method == 'GET':
        clothes = models.Clothes.objects.filter().order_by('-id')
        context = {'clothes': clothes}
        return render(request, 'all_clothes_view.html', context=context)
    
def older_view(request):
    if request.method == 'GET':
        older = models.Clothes.objects.filter(tags__name='Для пожилых').order_by('-id')
        context = {'older': older}
        return render(request, 'older_view.html', context=context)
    
def younger_view(request):
    if request.method == 'GET':
        younger = models.Clothes.objects.filter(tags__name='Для молодых').order_by('-id')
        context = {'younger': younger}
        return render(request, 'younger_view.html', context=context)
    
def kids_view(request):
    if request.method == 'GET':
        kids = models.Clothes.objects.filter(tags__name='Для детей').order_by('-id')
        context = {'kids': kids}
        return render(request, 'kids_view.html', context=context)
