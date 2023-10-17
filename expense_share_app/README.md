# create environment
python3 -m venv localenv
# activate environment
source localenv/bin/activate
# install django
pip install django
# install django-restframework
pip install djangorestframework
# run migrations and migrate
python3 manage.py makemigrations && python3 manage.py migrate
# run project
python3 manage.py runserver