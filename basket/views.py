from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from .forms import OrderForm

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_list')  
    else:
        form = OrderForm()
    return render(request, 'basket/create_order.html', {'form': form})

def order_list(request):
    orders = models.Order.objects.all().order_by('-id')
    return render(request, 'basket/order_list.html', {'orders': orders})

def edit_order(request, order_id):
    order = get_object_or_404(models.Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'basket/edit_order.html', {'form': form})

def delete_order(request, order_id):
    order = get_object_or_404(models.Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'basket/delete_order.html', {'order': order})
