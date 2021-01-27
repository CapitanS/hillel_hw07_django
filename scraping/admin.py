from django.contrib import admin

# Register your models here.
from .models import Authors, Quotes


class QuotesInline(admin.TabularInline):
    """Defines format of inline quotes insertion (used in AuthorsAdmin)"""
    model = Quotes
    extra = 0


# Define the admin class
@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    """Administration object for Authors models.
        Defines:
         - fields to be displayed in list view (list_display)
         - adds inline addition of author instances in author view (inlines)
        """
    list_display = ('author_title', 'author_born_date', 'author_born_location', 'author_description')
    fields = ['author_title', ('author_born_date', 'author_born_location'), 'author_description']
    inlines = [QuotesInline]
    list_per_page = 10


# Define the Admin classes for Quotes
@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    """Administration object for Quotes models.
        Defines:
         - fields to be displayed in list view (list_display)
        """
    list_display = ('text', 'author',)
    list_filter = ('author',)
    list_per_page = 10
