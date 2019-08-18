from django.db import models

class cards(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    track=models.FileField(upload_to='album')
    desc=models.TextField()
    city=models.CharField(max_length=50)
    favourite=models.BooleanField(default=False)
# class Publication(models.Model):
#     title = models.CharField(max_length=30)

#     class Meta:
#         ordering = ('title',)

#     def __str__(self):
#         return self.title

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)

#     class Meta:
#         ordering = ('headline',)

#     def __str__(self):
#         return self.headline