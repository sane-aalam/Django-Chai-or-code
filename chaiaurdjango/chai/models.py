
# Create your models here.
# You have to create modles here -
# Django models are the heart of the Django framework. 
# They are used to define the structure of the database and the relationships between different models.
# In this section, we will explore the basics of Django models and how to create them.

# Fields?
# The most important part of a model – and the only required part of a model – is the list of database fields it defines. Fields are specified by class attributes. Be careful not to choose field names that conflict with the models API like clean, save, or delete.

# What is Migrations?
# - Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema

# Tuples(first-element,second-element)
# The first element in each tuple is the value that will be stored in the database.
# Tuples are immutable in nature. Thus, we cannot make changes after creating it.(basic python)
# CHAI_TYPE_CHOICES = [
#     ('ML', 'MASALA'),
#     ('GR', 'GINGER'),
#     ('KL', 'KIWI'),
#     ('PL', 'PLAIN'),
#     ('EL', 'ELAICHI'),
#   ]

# What is charField,TextField?
# CharField is a string field, for small- to large-sized strings. It is like a string field in C/C++. CharField is generally used for storing small strings like first name, last name, etc. To store larger text TextField is used. The default form widget for this field is TextInput.

# name: A CharField that stores the name of the chai variety.
# image: An ImageField that stores the image of the chai variety.
# date_added: A DateTimeField that stores the date and time when the chai variety was added.
# type: A CharField that stores the type of the chai variety (e.g., ‘ML’, ‘GR’, ‘KL’, ‘PL’, ‘EL’).
# description: A TextField that stores the description of the chai variety.

# Remember - Migrations we need to run, whenever Database is changed!
# (Django-Chai-or-code) C:\Users\HP\Desktop\Django-Chai-or-code\chaiaurdjango>python manage.py makemigrations chai
# Migrations for 'chai':
#   chai\migrations\0002_remove_chaivariety_first_name_and_more.py
#     - Remove field first_name from chaivariety
#     - Remove field last_name from chaivariety 

# python -m pip install Pillow -> can not use Imagefield becasue pillow is not installed.

# Relationships¶
# 1.one-one-relationship
# 2.one-to-many relationship
# 4.many-to-one realtionsip

from django.utils import timezone
from django.db import models

class ChaiVariety(models.Model):    
    CHAI_TYPES_CHOICES = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    current_date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPES_CHOICES,default='ML')
    
    # The __str__ method is used to return a string representation of the object. In this case, 
    # it returns the name of the chai variety.
    def __str__(self):
        return self.name
    
    
    