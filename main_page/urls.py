from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]