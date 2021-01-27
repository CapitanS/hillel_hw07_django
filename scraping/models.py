from django.db import models


# Create your models here.
class Quotes(models.Model):
    text = models.TextField()
    author = models.ForeignKey('Authors', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Quotes object."""
        return self.text

    class Meta:
        ordering = ['author']
        verbose_name_plural = 'Quotes'


class Authors(models.Model):
    author_title = models.CharField(max_length=100)
    author_born_date = models.CharField(max_length=100)
    author_born_location = models.CharField(max_length=200)
    author_description = models.TextField()

    def __str__(self):
        """String for representing the Authors object."""
        return f'{self.author_title}'

    class Meta:
        ordering = ['author_title', 'author_description']
        verbose_name_plural = 'Authors'
