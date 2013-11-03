from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birth_date = models.DateField()
    short_description = models.TextField(max_length=300)
    programming_langs = models.TextField(max_length=150)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Order(models.Model):
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    name = models.CharField()
    description = models.TextField()


class Project(models.Model):
    name = models.CharField()
    owner = models.CharField()
    description = models.TextField(max_length=200)


class StoredFile(models.Model):
    path = models.CharField()
    name = models.CharField()
    date = models.DateTimeField()
    extention = models.CharField()