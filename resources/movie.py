from flask import request
from flask_restful import Resource, Api
from http import HTTPStatus
import messages

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
                   price_for_rent = movie_details['price_for_rent'],
                   price_for_buy = movie_details['price_for_buy'],
                   count_rent = movie_details['count_rent'],
                   count_buy  = movie_details['count_buy'],
                   num_reviews = movie_details['num_reviews'],
                   is_available = movie_details['is_available'])

        movie_catalog.append(movie)
        print(movie.id)
        return movie.data, HTTPStatus.CREATED

class MovieResource(Resource):
    def get(self, movie_id):
        movie = next((movie for movie in movie_catalog if movie.id == movie_id and movie.is_available == True ), None)

        print("something")
        print(movie for movie in movie_catalog if movie.id == movie_id)

        if movie is None:
            return {'message' : messages.MOVIE_NOT_FOUND}, HTTPStatus.NOT_FOUND
    
        return movie.data, HTTPStatus.OK

    def put(self, movie_id):
        movie_details = request.get_json()

        movie = next((movie for movie in movie_catalog if movie.id == movie_id), None)

        if movie is None:
            return {'message' : messages.MOVIE_NOT_FOUND}, HTTPStatus.NOT_FOUND

        movie.name=movie_details['name']
        movie.image =movie_details['image']
        movie.alt =movie_details['alt']
        movie.rating =movie_details['rating']
        movie.url =movie_details['url']
        movie.genre_id =movie_details['genre_id']
        movie.price_for_rent =movie_details['price_for_rent']
        movie.price_for_buy =movie_details['price_for_buy']
        movie.count_rent =movie_details['count_rent']
        movie.count_buy  =movie_details['count_buy']
        movie.num_reviews =movie_details['num_reviews']   
        movie.is_available = movie_details['is_available']

        return movie.data, HTTPStatus.OK

    def delete(self, movie_id):
        movie = next((movie for movie in movie_catalog if movie.id == movie_id), None)

        if movie is None:
            return {'message' : messages.MOVIE_NOT_FOUND}, HTTPStatus.NOT_FOUND
        
        movie.is_available = False

        return {}, HTTPStatus.NO_CONTENT


