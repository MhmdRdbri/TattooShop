# Generated by Django 4.2.4 on 2023-09-22 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
