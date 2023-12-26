"# Bookshop" 
 ## Django Book Library Project

This project is a simple Django application that allows users to manage a library of books. It includes models for genres, authors, and books, as well as views for creating, reading, updating, and deleting books.

### Prerequisites

To run this project, you will need:

* Python 3.6 or later
* Django 3.0 or later
* A database (such as PostgreSQL or MySQL)

### Installation

1. Clone the project repository:

```bash
git clone https://github.com/Mashaun18/Bookshop.git
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

4. Create a database and migrate the models:

```bash
createdb django_book_library
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

### Usage

To use the application, simply visit the following URLs:

* `/books/` to view a list of all books
* `/books/create/` to create a new book
* `/books/<slug>/` to view the details of a specific book
* `/books/<slug>/update/` to update the details of a specific book
* `/books/<slug>/delete/` to delete a specific book

### Code Overview

The code for this project is organized into the following files:

* `models.py` contains the Django models for genres, authors, and books.
* `views.py` contains the Django views for creating, reading, updating, and deleting books.
* `urls.py` contains the Django URL patterns for the application.
* `settings.py` contains the Django settings for the project.

### Models

The `Genre` model represents a genre of books. It has a single field, `name`, which is a character field with a maximum length of 100 characters.

```python
class Genre(models.Model):
    name = models.CharField(max_length=100)
```

The `Author` model represents an author of books. It has a single field, `name`, which is a character field with a maximum length of 200

