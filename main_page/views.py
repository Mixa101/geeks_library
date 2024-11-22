from django.shortcuts import get_object_or_404, redirect
from . import models, forms
from django.views import generic

class BookList(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books'
    def get_queryset(self):
        return models.Books.objects.all()

class BookDetail(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book'
    model = models.Books
    pk_url_kwarg = 'book_id'
    form_class = forms.CommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = context['book'].comments.all()
        return context


class CommentView(generic.CreateView):
    model = models.Comment
    form_class = forms.CommentForm
    template_name = 'add_comments.html'
    
    
    def form_valid(self, form):
        book_id = self.kwargs['book_id']
        book = get_object_or_404(models.Books, id=book_id)
        comment = form.save(commit=False)
        comment.book = book
        comment.save()
        return redirect('book_detail', book_id=book_id)
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            book_id = self.kwargs['book_id']
            context['book'] = get_object_or_404(models.Books, id=book_id)
            return context
        


