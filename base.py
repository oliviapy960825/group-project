import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

# define database tables
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    director = db.Column(db.String(64))
    actors = db.Column(db.String(64))
    description = db.Column(db.Text)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.Text)
    movies = db.relationship('Movie', backref='genre',cascade="delete")##back reference at the many side, unique in ORM

@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the home page!<h1>"
    return render_template('home-base.html')


@app.route('/members')
def show_all_members():
    # return "<h2>this is the page for all members</h2>"
    return render_template('member-all.html')

@app.route('/genres')
def show_all_genres():
    genres = Genre.query.all()
    return render_template('genre-all.html', genres=genres)

@app.route('/genre/edit/<int:id>', methods=['GET', 'POST'])
def edit_genre(id):
    genre = Genre.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('genre-edit.html', genre=genre)
    if request.method == 'POST':
        # update data based on the form data
        genre.name = request.form['name']
        genre.description = request.form['description']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_genres'))

@app.route('/genre/delete/<int:id>', methods=['GET', 'POST'])
def delete_genre(id):
    genre = Genre.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('genre-delete.html', genre=genre)
    if request.method == 'POST':
        db.session.delete(genre)
        db.session.commit()
        return redirect(url_for('show_all_genres'))



@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)

@app.route('/movie/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    genre = Genre.query.all()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie, genre=genre)
    if request.method == 'POST':
        # update data based on the form data
        movie.name = request.form['name']
        movie.director = request.form['director']
        movie.actors = request.form['actors']
        movie.description = request.form['description']
        genre_name = request.form['genre']
        genre = Genre.query.filter_by(name=genre_name).first()
        movie.genre = genre
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_movies'))

@app.route('/movie/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    genre = Genre.query.all()
    if request.method == 'GET':
        return render_template('movie-delete.html', movie=movie, genre=genre)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))

# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
