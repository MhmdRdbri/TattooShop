# Generated by Django 4.2.4 on 2023-09-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0008_rename_description_patternimage_body_pattern_body_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('locale', models.CharField(blank=True, max_length=500, null=True, verbose_name='Og:locale')),
                ('type', models.CharField(blank=True, max_length=500, null=True, verbose_name='Og:type')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Og:title')),
                ('descriptionOg', models.CharField(blank=True, max_length=500, null=True, verbose_name='Og:description')),
                ('site_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Og:site_name')),
                ('width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:width')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Og:image:height')),
            ],
            options={
                'verbose_name': 'Course Page Tag',
                'verbose_name_plural': 'Course Page Tags',
            },
        ),
    ]
