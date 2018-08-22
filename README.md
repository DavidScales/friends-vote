# Friends Vote

A simple app for learning TDD & Python development. Built with Django. Inspired by [Obey the Testing Goat](http://www.obeythetestinggoat.com/), a truly amazing book on TDD, Python, and web development.

## Set up

Install [geckodriver](https://github.com/mozilla/geckodriver/releases), which is a proxy that allows us to control Firefox programmatically via Selenium.

Confirm installation:

```
geckodriver --version
```

Create a Python virtual environment, which enables us to configure & install a specific Python version and modules for the project directory:

```
python3.6 -m venv virtualenv
```

The `-m` flag tells Python to run the `venv` module directly (rather than as an imported library), and `virtualenv` is the directory name for the virtual environment files.

Activate the virtual environment:

```
source virtualenv/bin/activate
# deactivate with "deactivate"
```

Install Django and Selenium in the virtual environment:

```
pip install "django<1.12" "selenium<4"
```

Create a Django "project":

```
django-admin.py startproject friendsvoteproject .
```

And then create a Django "app":

```
python manage.py startapp friendsvoteapp
```

Dev server can be started with:

```
python manage.py runserver
```

Things to add to **.gitignore**:

```
db.sqlite3
geckodriver.log
virtualenv
__pycache__
*.pyc
```