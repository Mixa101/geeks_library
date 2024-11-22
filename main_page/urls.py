from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('books/<int:book_id>/', views.BookDetail.as_view(), name='book_detail'),
    path('books/add_comment/<int:book_id>', views.CommentView.as_view(), name='add_comment')
]