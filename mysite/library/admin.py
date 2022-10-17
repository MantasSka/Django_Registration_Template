from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, BookReview, Profile

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    readonly_fields = ('id',)
    can_delete = False
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back', 'reader', 'id', 'status')
    list_editable = ('due_back', 'status')
    list_filter = ('status', 'due_back')
    search_fields = ('id', 'book__title')
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_books')

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'date_created', 'reviewer', 'content')

admin.site.register(Book, BookAdmin) 
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Profile)
