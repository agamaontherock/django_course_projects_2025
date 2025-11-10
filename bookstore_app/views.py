from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.
class BooksView(generic.ListView):
    model = models.Book
    
class BookView(generic.DetailView):
    model = models.Book
    
class CreateBookView(generic.CreateView):
    model = models.Book
    fields = "__all__"
    
    
class UpdateBookView(generic.UpdateView):
    model = models.Book
    fields = "__all__"
