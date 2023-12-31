# Generated by Django 4.2.4 on 2023-09-28 06:12

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTags',
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
                ('extratag', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='تگ های جدید')),
                ('schema1', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='اسکیما')),
                ('schema2', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='اسکیما')),
            ],
            options={
                'verbose_name': 'Course Page Tag',
                'verbose_name_plural': 'Course Page Tags',
            },
        ),
    ]
