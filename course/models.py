from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    dynamic_attributes = models.JSONField()

    def __str__(self):
        return self.name