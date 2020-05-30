# Throtle_test_api
 ==================================
Throtle_test_api Django Application as an API
==================================
Django application with User and ActivityPeriod models, with a custom management page to populate the database with some dummy data.

Api can be found at http://sreeramsreekrishna.pythonanywhere.com/
For Adding Data visit at http://sreeramsreekrishna.pythonanywhere.com/home
For viewing data either go to http://sreeramsreekrishna.pythonanywhere.com/ and then click on the rest api link 
or 
visit this link directly to view data in json format http://sreeramsreekrishna.pythonanywhere.com/request/?format=json  



--------
Overview
--------

Django Web App will produce a response like:

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": "3",
        "real_name": "sree",
        "tz": "mumbai",
        "activity_periods": [
            {
                "start_time": "May 21 2020 00:00 AM",
                "end_time": "May 05 2020 00:00 AM"
            },
            {
                "start_time": "May 21 2020 00:00 AM",
                "end_time": "May 05 2020 00:00 AM"
            },
            {
                "start_time": "May 13 2020 00:00 AM",
                "end_time": "May 05 2020 00:00 AM"
            }
        ]
    }
 ]


------------
Requirements
------------

1. Python 3.6
2. Django 3.0
3. Django REST Framework (3.10, 3.11)

------------
Installation
------------

    $ pip install django
    $ # for optional package integrations
    $ pip install djangorestframework==3.11


Running the example app
^^^^^^^^^^^^^^^^^^^^^^^

It is recommended to create a virtualenv for testing. Assuming it is already
installed and activated:

::

    $ git clone https://github.com/ssk1881/Throtle_test_api
    $ cd Throtle_test_api
    $ pip install django
    $ pip install djangorestframework==3.11
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver 

Browse to http://localhost:8000

-----
Usage
-----
For Adding data to the api visit at http://sreeramsreekrishna.pythonanywhere.com/home
Fill the form and submit. Data will be stored in the database
Next for retrieval of data as a json visit at http://sreeramsreekrishna.pythonanywhere.com/request/?format=json

    
