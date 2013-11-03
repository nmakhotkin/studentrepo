from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    birth_date = models.DateField()
    short_description = models.TextField(max_length=300)
    programming_langs = models.TextField(max_length=150)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
