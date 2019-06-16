import json
from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import Movie,Genre

class Command(BaseCommand):

    def handle(self, *args, **options):
        file=settings.BASE_DIR + '/task_1.json'
        with open(file, 'r') as f_ptr:
            data_d =f_ptr.read()
            data = json.loads(data_d)
            dir={}
            for movie_data in data:
                dir['popularity'] = movie_data.get('99popularity')
                dir['director'] = movie_data.get('director')
                dir['imdb_score'] = movie_data.get('imdb_score')
                dir['name'] = movie_data.get('name')
                movie, m_data = Movie.objects.get_or_create(**dir)
                genres = movie_data.get('genre')
                for genre_n in genres:
                    genre_n = genre_n.strip()
                    genre, m_data =Genre.objects.get_or_create(name=genre_n)
                    movie.genre.add(genre)
                movie.save()
                #print(movie)