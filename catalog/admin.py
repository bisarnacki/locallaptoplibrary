from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Language, Book, BookInstance

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    def get_extra(self, request, obj=None, **kwargs):
    if obj.BookInstance.count() :
        return 0
    else:
        return 1

class BookInline(admin.TabularInline):
    model = Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)
admin.site.register(Language)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



