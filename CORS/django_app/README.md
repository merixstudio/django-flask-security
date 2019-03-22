To run this project:
1. clone repository `git clone https://github.com/merixstudio/django-flask-security.git`
2. Go to directory `cd /django\ &\ flask security/CORS/django_app/src`
3. Create virtual environment `virtualenv venv -p python3`
4. Activate it `source venv/bin/activate`
5. Install requirements `pip install -r requirements.txt`
6. Create database `touch db.sqlite3`
7. Run migrations `./manage.py runmigrations`
8. Create admin user `./manage.py createsuperuser`
9. Run project `./manage.py runserver`
10. Go to `http://localhost:8000/admin/` and log into your admin account
11. Create some sample data.
11. This data will be shared on `http://localhost:8000/api/v1/albums/` endpoint. You may optionally add album id to get single album instead of collecting all data.
