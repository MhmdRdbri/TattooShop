# Generated by Django 4.2.4 on 2023-09-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_tags_created_at_tags_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='canonical',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Canonical'),
        ),
    ]