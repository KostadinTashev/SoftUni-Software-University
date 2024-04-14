from django.db import models


class Post(models.Model):
    tite = models.CharField(
        max_length=30,
    )
