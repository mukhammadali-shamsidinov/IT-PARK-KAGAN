import uuid

from django.db import models

from users.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name

class Product(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} uuid:{self.id}"



class Lesson(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    title=models.CharField(max_length=150)
    url = models.TextField()

    def __str__(self):
        return self.title


class Video(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    video_url = models.ForeignKey(Lesson,on_delete=models.CASCADE)


    def __str__(self):
        return self.product.title

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    comment= models.TextField()


class Services(models.Model):
    img = models.ImageField(upload_to='services')
    title = models.CharField(max_length=100)
    description = models.TextField()

class MyBlog(models.Model):
    img = models.ImageField(upload_to='blog/')
    title = models.CharField()
    descr = models.TextField()

    def __str__(self):
        return self.title