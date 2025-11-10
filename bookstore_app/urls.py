from django.urls import path
from bookstore_app import views
urlpatterns = [
    path('books/', views.BooksView.as_view(), name="book-list"),
    path('books/<int:pk>', views.BookView.as_view(), name="book-detail"),
    path('books/new/', views.CreateBookView.as_view(), name="book-create"),
    path('books/<int:pk>/update', views.UpdateBookView.as_view(), name="book-update")
]
