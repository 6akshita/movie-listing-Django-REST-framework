from django.db import models
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    popularity = models.FloatField()
    director = models.CharField(max_length=100)
    imdb_score = models.FloatField()
    name = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
