from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    description = models.TextField()
    url = models.CharField(max_length=500, unique=True)
    created_at = DateTimeField(auto_now_add=True)
    cover_image = models.CharField(max_length=500, null=True, blank=True)
