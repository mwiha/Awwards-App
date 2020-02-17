import datetime as dt
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/')
    bio = models.TextField(default='Add a bio')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=1,
        related_name='profiles'
    )
    @classmethod
    def get_user_profile(cls,user):
        profile = Profile.objects.get(user=user)
        return profile

    def __str__(self):
        return f'{self.bio}'     

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    design = models.IntegerField(default=0,validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    link = models.URLField(max_length=200,null=True)
    usability = models.IntegerField(default=0,
    validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    content = models.IntegerField(default=0,
    validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    average = models.IntegerField(default=0,
    validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    project_pic = models.ImageField(upload_to='project_pic/')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='projects')
    
    @classmethod
    def get_user_projects(cls,profile):
        projects = cls.objects.filter(profile=profile)
        return projects
    
    @classmethod
    def get_overall_average(cls,projects):
        overall = 0
        for project in projects:
            overall += project.average
        try:
            average = overall/len(projects)
        except ZeroDivisionError:
            return 0
        return average
    
    @classmethod
    def search_projects(cls,search_term):
        projects = cls.objects.filter(name__icontains = search_term)
        return projects


    def __str__(self):
        return f'{self.name}'

class Voted(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def has_user_voted(cls,project,user):
        if cls.objects.filter(project=project,user=user):
            return True
        else:
            return False
    
    def __unicode__(self):
        return self.user
