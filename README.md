## group-project

#1. Setup Instructions:


Make sure to use Python version 2.7.x.

Install `virtualenv` if needed.

If you do not have a virtual environment yet on the project folder, set it up with:

    $ virtualenv venv

Then activate the virtual environment

    $ source venv/bin/activate

Install packages

    $ pip install -r requirements.txt

To initialize the database:

    $ python manage.py deploy

To run the development server (use `-d` to enable debugger and reloader):

    $ python manage.py runserver -d


#2.Project Design Information:

This project consists of a movie database, which includes a movie table and a genre table.

The columns of the movie table are id, name, director, actors, description, and genre.

The columns of the genre table are id, name, and description.

There is a one-to-many relationship between the genre table and the movie table. One movie can only have one genre while one genre can have many movies.
