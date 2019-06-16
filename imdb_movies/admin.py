from django.contrib import admin
from .models import Movie, Genre
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['popularity', 'director', 'imdb_score', 'name']
    list_filter = ['genre']
    search_fields = ['name', 'director']
    delete_confirmation_template = ['genre']
    fields = ['popularity', 'director', 'imdb_score', 'name']
    pass


class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)