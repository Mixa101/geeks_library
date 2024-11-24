from django.shortcuts import render
from .parse_data import create_data
from django.views import generic
from . import models

def create_litres_data(request):
    create_data()
    return render(request, 'succes_create.html')

class LitresList(generic.ListView):
    template_name = 'litres_list.html'
    context_object_name = 'litres'
    def get_queryset(self):
        return models.LitresModel.objects.all()