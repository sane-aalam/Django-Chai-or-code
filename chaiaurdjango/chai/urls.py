
from django.urls import path
from . import views

# Now, we need to make aware of this new urlpattern in our project’s urls.py file. Add the following code to the project’s urls.py file
# subUrls connects to main urls 
# easy to understand way - don't overthink,keep clean,clear

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
]