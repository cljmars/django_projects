from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

#admin.site.register(Book)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
#@admin.register = admin.site.register



#admin.site.register(Author)
# Define the author admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
# Register the admin class with the associated model



#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )










