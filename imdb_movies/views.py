from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializers
# Create your views here.


class MovieView(APIView):
    allowed_methods=['GET']
    serializer_class = MovieSerializers

    def get(self,request,*args,**kwargs):
        query = Movie.objects.all()

        name = request.query_params.get('name', None)
        if name is not None:
            query = query.filter(name__icontains=name)

        director = request.query_params.get('director', None)
        if director is not None:
            query = query.filter(director__icontains=director)

        # filter if movie has genre with queried genre name
        genre = request.query_params.get('genre', None)
        if genre is not None:
            query = query.filter(genre__name__icontains=genre)

        director = request.query_params.get('director', None)
        if director is not None:
            query = query.filter(director__icontains=director)

        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
