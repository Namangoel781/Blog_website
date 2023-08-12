from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ContactUsTb(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=90)
    phone = models.IntegerField()
    address = models.CharField(max_length=90)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    
class Popularblogs(models.Model):

    auth_name= models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    blog_title = models.CharField(max_length=100)
    content = RichTextField()
    


class Regularblogs(models.Model):

    auth_name= models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    blog_title = models.CharField(max_length=100)
    content = RichTextField()
    

