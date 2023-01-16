# This are steps to follow when creating Django project and applications
1. mkdir <name_of_your_foldder>
cd folder
2. create virtual env: python3 -m venv <name_of_env>
	python3 -m venv myenv
3. Activate the Env: source myenv/bin/activate
4. Installing django: pip install django
5. setting up your first Django project: django-admin startproject <name_of_project> - (myproject)
6. Run development server: python manage.py runserver
7. Migration - helps us to sync our apps data to be updated in the database
	command: python manage.py migrate
8. Create a super user: python manage.py createsuperuser
9. creating our first Django app: python manage.py startapp <app_name> - (myapp)
10. E-commerce: authenticatio, cart, payment, tracking - (services)
11. Django views handle HTTP request and response cycle
12. URL mapping /URLCong:
Django Models:
	#Database Relationships 
		- one to one eg. teacher and college
		- one to many eg. customer and vehicle
		- many to many eg teacher and subject
customer (name, email, phone_no)
vehicle (name, model, customer)
13 makemigrations and migrate,
python manage.py migrate
14. sqlmigrate. showmigrations
python manage.py sqlmigrate <app_name> 0001, 0002
python manage.py showmigrations
