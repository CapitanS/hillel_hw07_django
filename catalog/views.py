from catalog.models import Author, Book, BookInstance, Genre
from django.shortcuts import render
from django.views import generic


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Generate counts of books that contain word 'White'.
    num_wild_books = BookInstance.objects.filter(book__title__icontains='Wild').count()

    # Generate counts of genres that contain word 'Fiction'.
    num_fiction_genres = Genre.objects.filter(name__icontains='Fiction').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_wild_books': num_wild_books,
        'num_fiction_genres': num_fiction_genres,
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    """Generic class-based view for a book."""
    model = Book


class AuthorListView(generic.ListView):
    """Generic class-based view for a list of author."""
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    """Generic class-based view for a author."""
    model = Author
