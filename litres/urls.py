from . import views
from django.urls import path

urlpatterns = [
    path('litres/create/', views.create_litres_data, name='create_data'),
    path('litres/', views.LitresList.as_view(), name='litres_list')
]