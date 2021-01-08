from flask import request
from flask_restful import Resource, Api
from http import HTTPStatus

from models.movie import Movie, movie_catalog

class MovieCatalogResource(Resource):
    def get(self):
        movie_list = []

        for movie in movie_catalog:
            movie_list.append(movie.data)

        return {'data': movie_list}, HTTPStatus.OK
    
    def post(self):
        movie_details = request.get_json()

        #print(movie_details)

        movie = Movie(name=movie_details['name'],
                   image =movie_details['image'],
                   alt =movie_details['alt'],
                   rating =movie_details['rating'],
                   url =movie_details['url'],
                   genre_id =movie_details['genre_id'],
                   price_for_rent =movie_details['price_for_rent'],
                   price_for_buy =movie_details['price_for_buy'],
                   count_rent =movie_details['count_rent'],
                   count_buy  =movie_details['count_buy'],
                   num_reviews =movie_details['num_reviews'])

        movie_catalog.append(movie)

        return movie.data, HTTPStatus.CREATED