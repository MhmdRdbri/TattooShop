from django.db import models


class Pattern(models.Model):
    title = models.CharField(max_length=250)
    image