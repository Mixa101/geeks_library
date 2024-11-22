from django.urls import path
from . import views

urlpatterns = [
    path('backet/', views.BacketListView.as_view(), name='backet_list'),
    path('backet/create/', views.BacketCreateView.as_view(), name='backet_create'),
    path('backet/edit/<int:pk>', views.BacketUpdateView.as_view(), name='backet_edit'),
    path('backet/delete/<int:pk>', views.BacketDeleteView.as_view(), name='backet_delete'),
]