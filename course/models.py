from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    attributes = models.ManyToManyField('CourseAttribute', blank=True)

    def __str__(self):
        return self.name


class CourseAttribute(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name
