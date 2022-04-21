from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Material(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(max_length=200)
    photo = models.ImageField(upload_to='images/')
    add_date = models.DateTimeField(auto_now_add=True)
    distributors = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="materials",
        null=True,
        )
