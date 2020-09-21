# Setting up the project:
  1. Create virtual environment: `virtualenv venv -p python3 && source venv/bin/activate`
  2. Install requirements: `pip install -r requirements.txt`
  3. Copy and update .env file with your personal data: `cp .env.example .env`
  4. Migrate database: `python manage.py migrate`
  5. Create user: `python manage.py createsuperuser`
  6. Start server and go to http://localhost:8000/login/ to log in: `python manage.py runserver`
