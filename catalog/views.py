from datetime import datetime

from catalog.forms import RenewBookForm
from catalog.models import Author, Book, BookInstance, Genre, Person
from catalog.tasks import send_email_with_reminder
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import ContactForm, PersonModelForm, SendEmailModelForm


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

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_wild_books': num_wild_books,
        'num_fiction_genres': num_fiction_genres,
        'num_visits': num_visits,
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


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


# Renew book
@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    permission_required = 'catalog.can_mark_returned'
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    permission_required = 'catalog.can_mark_returned'
    fields = '__all__'  # Not recommended (potential security issue if more fields added)


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('authors')


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    permission_required = 'catalog.can_mark_returned'
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    permission_required = 'catalog.can_mark_returned'
    fields = '__all__'  # Not recommended (potential security issue if more fields added)


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('books')


# Homework 9. Create view for creating Person
def person_view(request):
    if request.method == 'POST':
        form = PersonModelForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            # person = form.save()
            person = Person.objects.get(email=email)
            return HttpResponseRedirect(person.get_absolute_url())
    else:
        form = PersonModelForm()
    return render(request, 'person_form.html', {'form': form})


# Homework 9. Create view for Person details.
def person_detail(request, pk):
    person_inst = get_object_or_404(Person, pk=pk)
    # If this is a POST request then process the ModelForm data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = PersonModelForm(request.POST, instance=person_inst)
        # Check if the form is valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('person-detail', args=[pk]))

    # If this is a GET (or any other method) create the default form.
    else:
        form = PersonModelForm(instance=person_inst)

    context = {'form': form,
               'person_inst': person_inst}
    return render(request, 'person_detail.html', context)


# Homework 13. Celery
def send_email(request):
    if request.method == 'POST':
        form = SendEmailModelForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            time_sending = form.cleaned_data['time_sending']
            send_email_with_reminder.apply_async((text, email), eta=time_sending)
            messages.success(request, f'{email} will be get this Reminder at {time_sending}!')
            return redirect('send-email')
    else:
        form = SendEmailModelForm()
    return render(request, 'catalog/send_email.html', {'form': form})


# Homework 19.
def contact_page(request):
    form = ContactForm()
    return render(request, 'contact.html', {'contactForm': form})


def post_contact(request):
    if request.method == 'POST' and request.is_ajax():
        form = ContactForm(request.POST)
        form.save()
        return JsonResponse({'success': True}, status=200)
    return JsonResponse({'success': False}, status=400)
