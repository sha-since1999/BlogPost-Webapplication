from django.conf import settings
from django.db import models

User=settings.AUTH_USER_MODEL
 
class BlogPost(models.Model):  #blogpost_set ->queryset .         
    #id=models.IntegerField(); #pk.
    #foreign key is use to create user sprate model obj like indivisual models.
    user= models.ForeignKey(User,default=1,null=True ,on_delete=models.SET_NULL)
    # if no_delete=CASCADE than on delete user all date user related data has been deleted.
    title=models.TextField()
    img=models.ImageField(upload_to='image/', blank =True ,null=True)
    
    slug=models.SlugField(unique=True) #hello world-> hello-world
    content = models.TextField(null=True, blank=True)
    # name = models.CharField(max_length=30);
    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url}/delete"








""" shell cmd to check and rem 
from import django.contrib.auth import get_user_model
User=get_user_models()
j=User.objects.all()
j.blogpost_set.all()

from blog.models import BlogPost
qs=BlogPost.objects.filter(user__id=j.id)
qs
"""


