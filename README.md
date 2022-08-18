see bookmarks under course forstuff
https://ordinarycoders.com/blog/article/add-a-custom-favicon-to-your-django-web-app
https://learndjango.com/tutorials/django-static-files#:~:text=Loading%20static%20files%20in%20a%20template%20is%20a,using%20a%20templates%2Fbase.html%20file%20for%20a%20Blog%20project.

grep -r "PRJ_SETTINGS" .

django-admin startproject ADaaS    # Ad as a Service
python -m venv venv
source .venv/bin/activate
pip install djangorestframework    # https://medium.com/django-rest/lets-build-a-basic-product-review-backend-with-drf-part-1-652dd9b95485
pip install django-filter
python manage.py startapp reviews
add the model, register with admin
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
	admin
	beheenmt@gmail.com
	Bcsi7120@
python manage.py runserver
create serializers.py
""" To make our objects available through the API, we need to perform a serialization. A serializer is a framework that allows complex data such as querysets and model instances to be converted to native Python data types. Then, these can then be easily rendered into JSON or other content types. The reverse process is called deserialization. The serializers work in a way similar to Django’s Form classes.

The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields and it will automatically generate validators for the serializer. """
create views.py
update the url
"""FlexFields (DRF-FF) for Django REST Framework is a package designed to provide a common baseline of functionality for dynamically setting fields and nested models within DRF serializers. This package is designed for simplicity, with minimal magic and entanglement with DRF's foundational classes.

https://github.com/rsinger86/drf-flex-fields"""

pip install drf-flex-fields
python manage.py runserver

python manage.py startapp auth
"""What is JWT?

JSON Web Token (JWT) is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWT used to create access tokens for an application. JWT is good for API authentication, and server-to-server authorization.

The server generates a token that certifies the user identity, and sends it to the client. The client will send the token back to the server for every subsequent request, so the server knows the request comes from a particular identity.
Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework. It aims to cover the most common use cases of JWTs by offering a conservative set of default features. It also aims to be easily extensible in case a desired feature is not present.
Header : Identifies which algorithm is used to generate the signature.
Payload : Contains a set of claims. Claims are statements about an entity. 
Signature : Securely validates the token.
add pic of JWT

"""
pip install djangorestframework-simplejwt
add jwt to settings, urls
created fixture to load initial data into category model
# You can load data (i.e. initial) by calling manage.py loaddata <fixturename>, where <fixturename> 
# is the name of the fixture file you have created. Each time you run loaddata, the data will be read 
# from the fixture and reloaded into the database. Note this means that if you change one of the rows 
# created by a fixture and then run loaddata again, you’ll wipe out any changes you have made.

pip install redis
python manage.py collectstatic

Apache deployment:
sudo apt-get update
sudo apt-get install apache2
sudo a2enmod wsgi
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
pip install uwsgi
apache conf in /etc/apache2/sites-available/adaas.conf
see wsgi.py
sudo chmod -R 777 /home/beheen/PROJECTS/ADaaS
sudo a2enmod headers - bu default apache CORS is off
sudo a2ensite adaas.conf
sudo systemctl reload apache2
sudo service apache2 start

got the bootstrap 4.6 and redo the css, created logo (16 text size) and favicon (12) in MSWord, tranfered to static/img 


https://dev.to/vlntsolo/how-to-split-django-settings-for-different-environments-18ad#:~:text=Add%20environment-specific%20settings%20Since%20we%20have%20base.py%2C%20we,variables%20instead%20of%20hard-coding%20them%20into%20your%20production.py.
# Beanstalk allows you to specify preferred settings in an environmental variable called DJANGO_SETTINGS_MODULE. 
# Thus, you can just tune your Beanstalk app to load respective configuration like this:
# DJANGO_SETTINGS_MODULE: "your_main_django_app.settings.production"

changed the project directory from ADaaS to PRJ_SETTINGS
to add map to contact page had to activate googlemap api under hydroclimate to get a key.