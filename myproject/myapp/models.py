from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    role = models.IntegerField()
    city = models.CharField(max_length=100)
    