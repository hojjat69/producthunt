# producthunt
The purpose of this website is the product hunting. Each user can upload his/her project after signup and login,then s/he may vote for favorite project of others. The back-end of the website is composed of two applications: 1. accounts application that handles user object with functionalities of signup, signin, signout. 2. product application that handles product object with functionalities of the uploading, voting and presentation of each project. The two objects (user and product) are communicating with each other during voting and uploading as an authentifier and identifier.




Steps to Visualize the Web:



1. You need to install Python as well as PostGreSQL on your computer to visualize the web. 

2. Setting a localdatabase: 

you should make changes to DATABASES of the setting.py >>

It requires user name and the password you have created during installation of PostGreSQL. Additionally, you need to install the Pgadmin
to create database with specific name and you need to enter this name next to the "NAME" section. At the end you need to set 
the localhost and the port according to what is given by PostGresSQL during installation.





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database name',
        'USER':'your user name',
        'PASSWORD':'your password',
        'HOST': 'localhost',
        'PORT': 'your port',
      }
    }
    
    
    
    
    

2. You will also need the connectors between Django and PostGreSQL which are called psycopg2 and pillow. you can use pip tools in python to install them by following command in cmd: 

   pip install psycopg2
   
   
   pip install pillow


3. You need to create migration by writing the following command in cmd:
   python manage.py makemigrations
   

4. The last stem is migration by writing the following command in the cmd:
   python manage.py migrate
  
  Now you should be able to see the migrated files in your local database. You need to install Pgadmin to see it in your local 
   database.

5. Now open cmd and set your dir to project folder and run the manage.py by python as follow:
   python manage.py runserver

6. Open your browser and browse http://127.0.0.1:8000/
  
Enjoy your browsning ;)  
 

