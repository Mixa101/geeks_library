from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import BacketForm
from .models import Order

class BacketListView(generic.ListView):
    template_name = 'backet_list.html'
    context_object_name = 'orders'
    def get_queryset(self):
        return Order.objects.all()

class BacketCreateView(generic.CreateView):
    template_name = 'backet_create.html'
    model = Order
    form_class = BacketForm
    
    def form_valid(self, form):
        form.save()
        return redirect('backet_list')

class BacketUpdateView(generic.UpdateView):
    model = Order
    form_class = BacketForm
    template_name = 'edit_backet.html'
    
    def form_valid(self, form):
        form.save()
        return redirect('backet_list')

class BacketDeleteView(generic.DeleteView):
    model = Order
    template_name = 'delet_backet.html'
    success_url = reverse_lazy('backet_list')
    