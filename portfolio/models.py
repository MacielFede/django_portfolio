from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class PortfolioInfo(models.Model):
    name = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100)
    degree_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')
    about_me = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name