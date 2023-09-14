# Generated by Django 4.2.4 on 2023-09-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_courseattribute_remove_course_dynamic_attributes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='attributes',
        ),
        migrations.AddField(
            model_name='course',
            name='dynamic_attributes',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.DeleteModel(
            name='CourseAttribute',
        ),
    ]
