from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from movieRecommender import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Movie(db.Model):
	movieId = db.Column(db.Integer, primary_key = True)
	rating = db.Column(db.Float, nullable = False)
	title = db.Column(db.String(500), nullable = False)
	director = db.Column(db.String(50), nullable = False)
	year = db.Column(db.Integer, nullable = False)
	revenue = db.Column(db.Integer, nullable=True)
	imdbLink = db.Column(db.String(100), nullable=True)
	runtime = db.Column(db.Float, nullable=True)
	tagline = db.Column(db.String(500), nullable=True)
	language = db.Column(db.String(20), nullable=True)
	posterPath = db.Column(db.String(50), nullable=True)
	overview = db.Column(db.String(1000), nullable=True)
	voteCount = db.Column(db.Float, nullable=True)

	def __repr__(self):
		return f"Movie('{self.movieId}', '{self.rating}', '{self.title}', '{self.director}', '{self.year}', '{self.runtime}', '{self.imdbLink}')"

class Genre(db.Model):
	genreId = db.Column(db.Integer, primary_key = True)
	genreName = db.Column(db.String(50),nullable = False)

	def __repr__(self):
		return f"Genre('{self.genreId}', '{self.genreName}')"

class MovieHasGenre(db.Model):
	movieHasGenreId = db.Column(db.Integer, nullable = False, primary_key=True)
	movieId = db.Column(db.Integer, db.ForeignKey('movie.movieId'), nullable = False)
	genreId = db.Column(db.Integer, db.ForeignKey('genre.genreId'), nullable = False, primary_key=True)

	def __repr__(self):
		return f"MovieHasGenre('{self.movieId}', '{self.genreId}')"

class Keyword(db.Model):
	keywordId = db.Column(db.Integer, primary_key = True)
	keywordName = db.Column(db.String(50),nullable = False)

	def __repr__(self):
		return f"Keyword('{self.keywordId}', '{self.keywordName}')"

class MovieHasKeyword(db.Model):
	movieHasKeywordId = db.Column(db.Integer, nullable=False, primary_key=True)
	movieId = db.Column(db.Integer, db.ForeignKey('movie.movieId'), nullable = False)
	keywordId = db.Column(db.Integer, db.ForeignKey('keyword.keywordId'), nullable = False, primary_key=True)

	def __repr__(self):
		return f"MovieHasKeyword('{self.movieId}', '{self.keywordId}')"

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(50), unique = True, nullable = False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable = False)

	def __repr__(self):
		return f"User('{self.id}', '{self.username}')"


class Watched(db.Model):
	watchedId = db.Column(db.Integer, primary_key = True)
	userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	movieId = db.Column(db.Integer, db.ForeignKey('movie.movieId'), nullable = False)

	def __repr__(self):
		return f"Watched('{self.watchedId}', '{self.userId}', '{self.movieId}')"

