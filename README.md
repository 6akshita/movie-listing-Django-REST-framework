# movie-listing-Django-REST-framework

Movie Listing API

An API interface to search and find movies by namesand directors.

It uses data from task_1.json

Setting up project and initializing data

pip install -r reuqirements.txt

./manage.py migrate

./manage.py runserver 8080

./manage.py imdb_movies

API request examples

User can only view the movies.

base API url - https://movielistingrestapi.herokuapp.com/api/movies

filter by movie name and director name https://movielistingrestapi.herokuapp.com/api/movies?name=hawaii&director=michael


Admin can add/delete/update the movie.

https://movielistingrestapi.herokuapp.com/admin/
