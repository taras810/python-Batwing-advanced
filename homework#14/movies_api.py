import http

from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError

from database import db
from models.movies import Movies
from serializers.movies import MovieSchema

movies_router = Blueprint('movie', __name__, url_prefix='/movie')


@movies_router.route('')
def get():
    movies_schema = MovieSchema()

    movies = Movies.query.order_by(Movies.title)
    movies_json = movies_schema.dump(movies, many=True)
    return jsonify(movies_json)


@movies_router.route('/<int:id_>')
def retrieve(id_):
    movies_schema = MovieSchema()
    movies = Movies.query.filter_by(id=id_).first()
    movies_json = movies_schema.dump(movies)
    return jsonify(movies_json)


@movies_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = MovieSchema()
    try:
        movie_data = schema.load(data)
        new_movie = Movies(title=movie_data['title'])
        db.session.add(new_movie)
        db.session.commit()

        new_movies_json = schema.dump(new_movie)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_movies_json


@movies_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = MovieSchema()
    try:
        movie_data = schema.load(data)
        movie = Movies.query.filter_by(id=id_).first()
        movie.title = movie_data['title']
        db.session.add(movie)
        db.session.commit()

        new_movies_json = schema.dump(movie)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_movies_json


@movies_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Movies.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT
