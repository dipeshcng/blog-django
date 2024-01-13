from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    gallery = models.ImageField(upload_to="event")
    description = models.TextField()
    organizer = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "(" + self.organizer + ")"


class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category")

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="news")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="relatednews")
    # category = models.ManyToManyField(Category)
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    messagge = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commenter
