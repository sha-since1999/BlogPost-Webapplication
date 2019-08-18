from django.urls import path #url

from account.views import logout

from .views import (index,register,login,)                       

urlpatterns = [ 
    path('',index,name='index'),
    path('logout',logout,name='logout'),

    path('register',register),
    path('login',login),
   
]
 