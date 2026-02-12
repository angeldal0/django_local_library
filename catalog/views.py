from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Modify the view to generate counts for genres and books that contain a particular word 
    # (case insensitive), and pass the results to the context. You accomplish this in a similar 
    # way to creating and using num_books and num_instances_available. Then update the index 
    # template to include these variables.
    num_genres = Genre.objects.count()

    books_contains_word = Book.objects.filter(summary__icontains='la').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'books_contains_word': books_contains_word
    }


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)