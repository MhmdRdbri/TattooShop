# Generated by Django 4.2.4 on 2023-09-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0004_alter_samples_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samples',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='اسلاگ'),
        ),
    ]