from django.contrib import admin

# Register your models here.
from .models import Author, Book, BookInstance, Genre, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    # TODO write description
    model = Book
    extra = 0


# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # TODO write description
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class BookInstanceInline(admin.TabularInline):
    # TODO write description
    model = BookInstance
    extra = 0


# Define the Admin classes for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # TODO write description
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


# Define the Admin classes for BookInstance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # TODO write description
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
