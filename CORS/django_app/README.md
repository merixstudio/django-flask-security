To run this project:
1. clone repository `git clone https://github.com/merixstudio/django-flask-security.git`
2. Go to directory `cd /django\ &\ flask security/CORS/django_app/src`
3. Create virtual environment `virtualenv venv -p python3`
4. Create database `touch db.sqlite3`
5. Run migrations `./manage.py runmigrations`
6. Create admin user `./manage.py createsuperuser`
7. Run project `./manage.py runserver`
8. Go to `http://localhost:8000/admin/` and log into your admin account
9. Create some sample data.
10. This data will be shared on `http://localhost:8000/api/v1/albums/` endpoint. You may optionally add album id to get single album instead of collecting all data.
