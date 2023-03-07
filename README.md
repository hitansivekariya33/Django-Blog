# Django-Blog
To get this project and running locally on your computer:

## setup the project 
  Copy 'env.example' to '.env' file and set the secret variable 

## Create python environment  
   python -m venv venv 

## Activate the virtual environment
   Source venv/bin/activate

## Insatll dependencies 
   pip install -r requirements.txt

## Apply the migrations
   python manage.py makemigrations
   python manage.py migrate 

## Create superuser 
   python manage.py createsuperuser

## Run the project 
   python manage.py runserver 

## Run the testcases
   python manage.py test blog.tests 

If you using python3 please replace the 'python' with 'python3'