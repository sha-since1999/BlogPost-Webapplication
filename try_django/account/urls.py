from django.urls import path #url

from sahuweb.views import index
from .views import (registration ,login,)                     

urlpatterns = [ 
    path('register',registration,name='registration'),
    path('login',login,name='login'),
    
   ]
 