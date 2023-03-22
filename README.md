# our-practice-app

python version 3.9.14

pyenv install -v 3.9.14
pyenv local 3.9.14
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
python manage.py startapp site_main