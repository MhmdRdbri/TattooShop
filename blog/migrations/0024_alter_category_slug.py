# Generated by Django 4.2.4 on 2023-09-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(default='slug', max_length=120, unique=True, verbose_name='اسلاگ'),
        ),
    ]
