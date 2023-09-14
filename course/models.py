from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دوره")
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = "دوره ها"

    def __str__(self):
        return self.name


class CourseAttribute(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, verbose_name="نام ویژگی")
    value = models.CharField(max_length=255, verbose_name="مقدار ویژگی")

    def __str__(self):
        return f"{self.course.name} - {self.key}: {self.value}"

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = "ویژگی ها"
