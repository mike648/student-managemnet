# StudentManagentSystem
Simple django project for CRUD operation using MySQL

# Make virtual environment for install packages, plugins and dependencies ...
mkvirtualenv env

# Activate virtual environment
workon env or env\scripts\activate

# installation
pip install -r requirements.txt

# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run server to view the Project
python manage.py runserver