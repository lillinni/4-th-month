from basket.models import Order
from basket.forms import OrderForm
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

class OrderListView(generic.ListView):
    template_name = 'basket/order_list.html'
    context_object_name = 'orders'
    model = Order

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')
    
class OrderCreateView(CreateView):
    template_name = 'basket/create_order.html'
    form_class = OrderForm
    success_url = '/order_list/'

    def from_valid(self, form):
        print(form.cleaned_data)
        return super(OrderCreateView, self).form_valid(form=form)

class OrderEditView(UpdateView):
    model = Order
    template_name = 'basket/edit_order.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')  

    def form_valid(self, form):
        print(form.cleaned_data)  
        return super().form_valid(form)  

    def get_object(self, queryset=None):
        order_id = self.kwargs.get('pk')  
        return get_object_or_404(Order, id=order_id)

    
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'basket/delete_order.html'
    success_url = reverse_lazy('order_list')  
    
    def get_object(self, queryset=None):
        order_id = self.kwargs.get('pk')  
        return get_object_or_404(Order, id=order_id)

    